"""Viincci-RAG UniversalResearchSpider — canonical import path.

This module re-exports UniversalResearchSpider as a viincci_rag-owned class that
inherits from the legacy V4.Spider.UniversalResearchSpider, making viincci_rag the primary
import path while maintaining backward compatibility.
"""
try:
    from V4.Spider import UniversalResearchSpider as _V4UniversalResearchSpider  # type: ignore
    
    class UniversalResearchSpider(_V4UniversalResearchSpider):  # type: ignore
        """UniversalResearchSpider for viincci_rag (inherits from V4.Spider.UniversalResearchSpider).
        
        This is the canonical UniversalResearchSpider for the viincci_rag package.
        It extends the V4 implementation without changing its behavior,
        making viincci_rag the primary import path.
        """
        pass

except Exception:  # pragma: no cover - fallback stub
    class UniversalResearchSpider:  # type: ignore
        def __init__(self, *args, **kwargs):
            raise RuntimeError("UniversalResearchSpider is unavailable. Import of V4.Spider failed.")

__all__ = ["UniversalResearchSpider"]
