"""Utilities compatibility package

Provides utility functions and classes re-exported from V4 for backward
compatibility.
"""

try:
    from V4.utils import (  # type: ignore
        content_cleaner,
        image_fetcher,
        validators,
    )
except Exception:  # pragma: no cover
    content_cleaner = None
    image_fetcher = None
    validators = None

__all__ = [
    "content_cleaner",
    "image_fetcher",
    "validators",
]
