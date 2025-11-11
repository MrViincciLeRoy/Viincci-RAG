"""Wrapper for V4.Spider.UniversalResearchSpider
"""
try:
    from V4.Spider import UniversalResearchSpider  # type: ignore
except Exception:  # pragma: no cover - fallback stub
    class UniversalResearchSpider:  # type: ignore
        def __init__(self, *args, **kwargs):
            raise RuntimeError("UniversalResearchSpider is unavailable. Import of V4.Spider failed.")

__all__ = ["UniversalResearchSpider"]
