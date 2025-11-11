"""Viincci-RAG RAGSystem — canonical import path.

This module re-exports RAGSystem as a viincci_rag-owned class that
inherits from the legacy V4.RagSys.RAGSystem, making viincci_rag the primary
import path while maintaining backward compatibility.
"""
try:
    from V4.RagSys import RAGSystem as _V4RAGSystem  # type: ignore
    
    class RAGSystem(_V4RAGSystem):  # type: ignore
        """RAGSystem for viincci_rag (inherits from V4.RagSys.RAGSystem).
        
        This is the canonical RAGSystem for the viincci_rag package.
        It extends the V4 implementation without changing its behavior,
        making viincci_rag the primary import path.
        """
        pass

except Exception:  # pragma: no cover - fallback stub
    class RAGSystem:  # type: ignore
        def __init__(self, *args, **kwargs):
            raise RuntimeError("RAGSystem is unavailable. Import of V4.RagSys failed.")

__all__ = ["RAGSystem"]
