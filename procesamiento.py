"""Entry point to build artifacts for the Metal Veneta thesis project."""

from __future__ import annotations

import json
from pathlib import Path

from analysis import compute_rendimiento_scenarios
from analysis.config import load_rendimiento_config
from data import load_materia_prima_table

ARTIFACTS_DIR = Path("artifacts")
OUTPUT_JSON = ARTIFACTS_DIR / "rendimientos_hipoteticos.json"


def main() -> None:
    dataset = load_materia_prima_table()
    config = load_rendimiento_config()
    resultados = compute_rendimiento_scenarios(dataset.table, config)

    # Seleccionamos columnas clave para el dashboard. Se puede ajustar más adelante.
    columnas_a_exportar = [
        "codigo",
        "nombre",
        "clasificacion",
        "formato",
        "rendimiento_base",
        "rendimiento_nueva_linea",
        "delta_rendimiento_pct",
        "peso_procesado",
        "peso_salida_base",
        "peso_salida_nueva_linea",
        "delta_peso_salida",
    ]

    exportable = resultados[columnas_a_exportar].to_dict(orient="records")

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(exportable, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Archivo generado en {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
