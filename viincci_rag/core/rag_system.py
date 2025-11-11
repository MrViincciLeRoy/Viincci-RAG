"""Wrapper for V4.RagSys.RAGSystem
"""
try:
    from V4.RagSys import RAGSystem  # type: ignore
except Exception:  # pragma: no cover - fallback stub
    class RAGSystem:  # type: ignore
        def __init__(self, *args, **kwargs):
            raise RuntimeError("RAGSystem is unavailable. Import of V4.RagSys failed.")

__all__ = ["RAGSystem"]
