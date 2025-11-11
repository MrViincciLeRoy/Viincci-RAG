"""Viincci-RAG SerpAPIMonitor — canonical import path.

This module re-exports SerpAPIMonitor as a viincci_rag-owned class that
inherits from the legacy V4.ApiMonitor.SerpAPIMonitor, making viincci_rag the primary
import path while maintaining backward compatibility.
"""
try:
    from V4.ApiMonitor import SerpAPIMonitor as _V4SerpAPIMonitor  # type: ignore
    
    class SerpAPIMonitor(_V4SerpAPIMonitor):  # type: ignore
        """SerpAPIMonitor for viincci_rag (inherits from V4.ApiMonitor.SerpAPIMonitor).
        
        This is the canonical SerpAPIMonitor for the viincci_rag package.
        It extends the V4 implementation without changing its behavior,
        making viincci_rag the primary import path.
        """
        pass

except Exception:  # pragma: no cover - fallback stub
    class SerpAPIMonitor:  # type: ignore
        def __init__(self, *args, **kwargs):
            raise RuntimeError("SerpAPIMonitor is unavailable. Import of V4.ApiMonitor failed.")

__all__ = ["SerpAPIMonitor"]
