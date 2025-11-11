"""Viincci-RAG ConfigManager — canonical import path.

This module re-exports ConfigManager as a viincci_rag-owned class that
inherits from the legacy V4.ConfigManager, making viincci_rag the primary
import path while maintaining backward compatibility.
"""
try:
    from V4.ConfigManager import ConfigManager as _V4ConfigManager  # type: ignore
    
    class ConfigManager(_V4ConfigManager):  # type: ignore
        """ConfigManager for viincci_rag (inherits from V4.ConfigManager).
        
        This is the canonical ConfigManager for the viincci_rag package.
        It extends the V4 implementation without changing its behavior,
        making viincci_rag the primary import path.
        """
        pass

except Exception:  # pragma: no cover - fallback stub
    class ConfigManager:  # type: ignore
        def __init__(self, *args, **kwargs):
            raise RuntimeError("ConfigManager is unavailable. Import of V4.ConfigManager failed.")

__all__ = ["ConfigManager"]
