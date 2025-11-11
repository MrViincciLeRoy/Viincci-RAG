"""Wrapper for V4.ConfigManager.ConfigManager
"""
try:
    from V4.ConfigManager import ConfigManager  # type: ignore
except Exception:  # pragma: no cover - fallback stub
    class ConfigManager:  # type: ignore
        def __init__(self, *args, **kwargs):
            raise RuntimeError("ConfigManager is unavailable. Import of V4.ConfigManager failed.")

__all__ = ["ConfigManager"]
