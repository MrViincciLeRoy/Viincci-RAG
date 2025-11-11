"""Wrapper for V4.UniversalArticleGenerator
"""
try:
    from V4.UniversalArticleGenerator import UniversalArticleGenerator  # type: ignore
except Exception:  # pragma: no cover - fallback stub
    class UniversalArticleGenerator:  # type: ignore
        def __init__(self, *args, **kwargs):
            raise RuntimeError("UniversalArticleGenerator is unavailable. Import of V4.UniversalArticleGenerator failed.")

__all__ = ["UniversalArticleGenerator"]
