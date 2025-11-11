"""Database compatibility package

Provides wrappers for database adapters. Currently re-exports from V4
for backward compatibility.
"""

try:
    from V4.FloraDatabase import FloraDatabase  # type: ignore
except Exception:  # pragma: no cover
    class FloraDatabase:  # type: ignore
        def __init__(self, *args, **kwargs):
            raise RuntimeError("FloraDatabase is unavailable.")

__all__ = ["FloraDatabase"]
