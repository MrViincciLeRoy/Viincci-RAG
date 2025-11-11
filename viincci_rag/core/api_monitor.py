"""Wrapper for V4.ApiMonitor.SerpAPIMonitor
"""
try:
    from V4.ApiMonitor import SerpAPIMonitor  # type: ignore
except Exception:  # pragma: no cover - fallback stub
    class SerpAPIMonitor:  # type: ignore
        def __init__(self, *args, **kwargs):
            raise RuntimeError("SerpAPIMonitor is unavailable. Import of V4.ApiMonitor failed.")

__all__ = ["SerpAPIMonitor"]
