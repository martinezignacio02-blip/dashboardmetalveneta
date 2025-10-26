"""Helpers to load analysis configuration from YAML files."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import yaml

from .metrics import RendimientoConfig

DEFAULT_CONFIG_PATH = Path("config") / "rendimiento_base.yaml"


def load_rendimiento_config(path: Path | None = None) -> RendimientoConfig:
    """Load hypothetical improvement settings from YAML."""

    config_path = Path(path or DEFAULT_CONFIG_PATH)
    if not config_path.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo de configuración {config_path}"
        )

    with config_path.open("r", encoding="utf-8") as fh:
        raw: Mapping[str, Any] = yaml.safe_load(fh) or {}

    default_delta = float(raw.get("default_delta_pct", 0.0))
    overrides = raw.get("overrides_pct") or {}

    return RendimientoConfig(
        default_delta_pct=default_delta,
        overrides_pct={str(k): float(v) for k, v in overrides.items()},
    )

