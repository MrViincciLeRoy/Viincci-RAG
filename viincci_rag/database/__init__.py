"""Viincci-RAG Database adapters — canonical import path.

Provides wrappers for database adapters. Exports FloraDatabase as a viincci_rag-owned
class that inherits from V4, making viincci_rag the primary import path while maintaining
backward compatibility with the legacy V4 package.
"""

try:
    from V4.FloraDatabase import FloraDatabase as _V4FloraDatabase  # type: ignore
    
    class FloraDatabase(_V4FloraDatabase):  # type: ignore
        """FloraDatabase for viincci_rag (inherits from V4.FloraDatabase).
        
        This is the canonical FloraDatabase for the viincci_rag package.
        It extends the V4 implementation without changing its behavior,
        making viincci_rag the primary import path.
        """
        pass

except Exception:  # pragma: no cover
    class FloraDatabase:  # type: ignore
        def __init__(self, *args, **kwargs):
            raise RuntimeError("FloraDatabase is unavailable.")

__all__ = ["FloraDatabase"]
