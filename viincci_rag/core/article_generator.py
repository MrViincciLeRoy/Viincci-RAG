"""Viincci-RAG UniversalArticleGenerator — canonical import path.

This module re-exports UniversalArticleGenerator as a viincci_rag-owned class that
inherits from the legacy V4.UniversalArticleGenerator, making viincci_rag the primary
import path while maintaining backward compatibility.
"""
try:
    from V4.UniversalArticleGenerator import UniversalArticleGenerator as _V4UniversalArticleGenerator  # type: ignore
    
    class UniversalArticleGenerator(_V4UniversalArticleGenerator):  # type: ignore
        """UniversalArticleGenerator for viincci_rag (inherits from V4.UniversalArticleGenerator).
        
        This is the canonical UniversalArticleGenerator for the viincci_rag package.
        It extends the V4 implementation without changing its behavior,
        making viincci_rag the primary import path.
        """
        pass

except Exception:  # pragma: no cover - fallback stub
    class UniversalArticleGenerator:  # type: ignore
        def __init__(self, *args, **kwargs):
            raise RuntimeError("UniversalArticleGenerator is unavailable. Import of V4.UniversalArticleGenerator failed.")

__all__ = ["UniversalArticleGenerator"]
