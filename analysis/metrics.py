"""Transformations to compare base vs. nueva línea performance scenarios."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Mapping

import pandas as pd

REQUIRED_COLUMNS = {
    "codigo",
    "nombre",
    "clasificacion",
    "formato",
    "rendimiento_base",
    "peso_procesado",
}


@dataclass
class RendimientoConfig:
    """Configuration for hypothetical improvements in the nueva línea."""

    default_delta_pct: float = 0.05
    overrides_pct: Mapping[str, float] = field(default_factory=dict)

    def delta_for(self, codigo: str) -> float:
        """Return the porcentaje adicional for a given código."""
        codigo_clean = (codigo or "").strip()
        if codigo_clean in self.overrides_pct:
            return self.overrides_pct[codigo_clean]
        return self.default_delta_pct


def _ensure_numeric(table: pd.DataFrame, column: str) -> pd.Series:
    series = pd.to_numeric(table[column], errors="coerce")
    return series.fillna(0.0)


def compute_rendimiento_scenarios(
    table: pd.DataFrame, config: RendimientoConfig | None = None
) -> pd.DataFrame:
    """Attach nueva línea KPIs to the materia prima dataset."""

    missing = REQUIRED_COLUMNS.difference(table.columns)
    if missing:
        raise KeyError(
            "Faltan columnas para calcular los escenarios de rendimiento: "
            + ", ".join(sorted(missing))
        )

    cfg = config or RendimientoConfig()

    enriched = table.copy()
    enriched["rendimiento_base"] = _ensure_numeric(enriched, "rendimiento_base")
    enriched["peso_procesado"] = _ensure_numeric(enriched, "peso_procesado")
    if "peso_salida_base" in enriched.columns:
        enriched["peso_salida_base"] = _ensure_numeric(enriched, "peso_salida_base")
    else:
        enriched["peso_salida_base"] = enriched["peso_procesado"] * enriched["rendimiento_base"]

    overrides: Dict[str, float] = dict(cfg.overrides_pct)
    enriched["mejora_pct"] = enriched["codigo"].map(
        lambda codigo: overrides.get(str(codigo).strip(), cfg.default_delta_pct)
    )

    # SUMAR la mejora al rendimiento base (no multiplicar)
    # mejora_pct contiene valores como 0.05 (5%), se suma directamente
    enriched["rendimiento_nueva_linea"] = (
        enriched["rendimiento_base"] + enriched["mejora_pct"]
    )
    
    # Si ya tenemos peso_salida_base, calcular la nueva usando el nuevo rendimiento
    # Si no, calcularlo a partir de peso_procesado y rendimiento
    if "peso_salida_base" in enriched.columns:
        # Calcular el nuevo peso de salida usando el nuevo rendimiento
        enriched["peso_salida_nueva_linea"] = (
            enriched["peso_procesado"] * enriched["rendimiento_nueva_linea"]
        )
    else:
        enriched["peso_salida_nueva_linea"] = (
            enriched["peso_procesado"] * enriched["rendimiento_nueva_linea"]
        )
    enriched["delta_rendimiento_pct"] = enriched["rendimiento_nueva_linea"] - enriched["rendimiento_base"]
    enriched["delta_peso_salida"] = (
        enriched["peso_salida_nueva_linea"] - enriched["peso_salida_base"]
    )
    enriched["mejora_pct_relativa"] = (
        enriched["delta_rendimiento_pct"] / enriched["rendimiento_base"].replace(0, pd.NA)
    )

    return enriched

