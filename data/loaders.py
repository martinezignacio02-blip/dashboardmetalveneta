"""Utilities to load the Metal Veneta raw material dataset."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import pandas as pd

LOGGER = logging.getLogger(__name__)

# Determinar la ruta del proyecto (directorio raíz)
if __file__.endswith('.pyc'):
    PROJECT_ROOT = Path(__file__).parent.parent.parent
else:
    PROJECT_ROOT = Path(__file__).parent.parent

DEFAULT_SOURCE = PROJECT_ROOT / "Materia Prima Metal Veneta.xlsx"
DEFAULT_SHEET = "Hoja1"

# Mapping to normalize column names we plan to use downstream. The Excel file
# includes accents and some trailing spaces; we strip and map them here so the
# rest of the pipeline can work with predictable identifiers.
COLUMN_ALIASES = {
    "Índice": "indice",
    "Indice": "indice",
    "Código": "codigo",
    "Código ": "codigo",
    "Clasificación": "clasificacion",
    "Clasificacion": "clasificacion",
    "Formato": "formato",
    "Nombre": "nombre",
    "Rend_min_%": "rendimiento_base",
    "Rend_max_%": "rendimiento_max",
    "Peso de salida": "peso_salida_base",
    "Peso procesado (kg)": "peso_procesado",
    "Peso perdido": "peso_perdido_base",
    "Volumen de salida": "volumen_salida",
}

# Columnas a crear derivadas
# Usaremos Formato como clasificacion para mantener compatibilidad


@dataclass
class MateriaPrimaSchema:
    """Container for the raw material dataset after initial cleaning."""

    table: pd.DataFrame


def load_materia_prima_table(
    source: Path = DEFAULT_SOURCE,
    sheet_name: str = DEFAULT_SHEET,
    *,
    rename_columns: bool = True,
) -> MateriaPrimaSchema:
    """Load the Excel workbook and return the primary sheet as a DataFrame.

    Parameters
    ----------
    source:
        Path to the Excel file downloaded from Metal Veneta.
    sheet_name:
        Name of the worksheet that contains the raw material catalogue.
    rename_columns:
        When true, normalize column names using COLUMN_ALIASES. Columns without
        an explicit mapping are stripped of whitespace but otherwise untouched.
    """

    source_path = Path(source)
    if not source_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo {source_path}")

    LOGGER.debug("Loading raw material table from %s (%s)", source_path, sheet_name)
    # Leer el archivo con header en la fila 0
    table = pd.read_excel(source_path, sheet_name=sheet_name, header=0)

    if rename_columns:
        normalized = {}
        for raw_col in table.columns:
            cleaned = str(raw_col).strip()
            normalized[raw_col] = COLUMN_ALIASES.get(cleaned, cleaned)
        table = table.rename(columns=normalized)
        
        # Si hay columnas duplicadas, quedarnos solo con la primera
        table = table.loc[:, ~table.columns.duplicated()]
    
    # Limpiar columnas numéricas: convertir comas a puntos
    numeric_cols = ['rendimiento_base', 'rendimiento_max', 'peso_procesado', 'peso_salida_base', 'peso_perdido_base']
    for col in numeric_cols:
        if col in table.columns:
            table[col] = table[col].astype(str).str.replace(',', '.').replace('nan', '')
            table[col] = pd.to_numeric(table[col], errors='coerce').fillna(0)
    
    # Convertir rendimientos de porcentaje (0.02 = 2%) a decimal (0.02 representa 2%)
    # Ya están en el formato correcto, pero si vienen como 2% (sin dividir por 100), lo dividimos
    # Asumimos que 0.02 significa 2%, no 200%
    
    # Crear columnas derivadas
    if "clasificacion" not in table.columns and "formato" in table.columns:
        table["clasificacion"] = table["formato"]
    
    # Si peso_salida_base tiene valores NaN y volumen_salida tiene valores, usar volumen_salida
    if "peso_salida_base" in table.columns and "volumen_salida" in table.columns:
        mask = table["peso_salida_base"].isna() | (table["peso_salida_base"] == 0)
        table.loc[mask, "peso_salida_base"] = table.loc[mask, "volumen_salida"]
        # Eliminar la columna volumen_salida ya que la hemos fusionado
        table = table.drop(columns=["volumen_salida"], errors='ignore')

    return MateriaPrimaSchema(table=table)

