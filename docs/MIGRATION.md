# Viincci-RAG Package Restructuring & Migration Guide

## Overview

The Viincci-RAG project has been restructured to follow Python packaging best practices while maintaining **full backward compatibility** with the legacy `V4` package. The new layout enables future modularization and makes the project installable via pip.

## Directory Structure

### Old Structure (V4)
```
V4/
├── __init__.py
├── ConfigManager.py
├── Spider.py
├── RagSys.py
├── UniversalArticleGenerator.py
├── ApiMonitor.py
├── FloraDatabase.py
├── FloraWikipediaScraper.py
├── ArtGenSys.py
├── utils.py
├── cli.py
├── config/
├── db/
└── test_v4.py
```

### New Structure (viincci_rag)
```
viincci_rag/
├── __init__.py              # Main entry point (re-exports from V4)
├── core/                    # Core RAG system modules
│   ├── __init__.py
│   ├── config.py           # ConfigManager wrapper
│   ├── rag_system.py       # RAGSystem wrapper
│   ├── spider.py           # UniversalResearchSpider wrapper
│   ├── article_generator.py # UniversalArticleGenerator wrapper
│   ├── api_monitor.py      # SerpAPIMonitor wrapper
│   └── ...
├── database/                # Database adapters
│   └── __init__.py
├── utils/                   # Utility functions
│   └── __init__.py
├── config/                  # Default configuration files
│   └── .gitkeep
├── templates/               # Output templates
│   └── __init__.py
└── cli.py                  # Command-line interface (future)

tests/
├── __init__.py
├── test_config.py
├── test_rag.py
├── test_spider.py
└── test_integration.py
```

## Backward Compatibility Strategy

### 1. **Wrapper Modules in `viincci_rag.core`**

Each core module in `viincci_rag.core` contains a **thin wrapper** that re-exports from the legacy `V4` package. This allows seamless migration:

**Example: `viincci_rag/core/rag_system.py`**
```python
try:
    from V4.RagSys import RAGSystem
except Exception:
    class RAGSystem:
        def __init__(self, *args, **kwargs):
            raise RuntimeError("RAGSystem is unavailable.")
```

### 2. **Multiple Import Paths**

All three import styles work identically:

```python
# Method 1: Legacy import (still works)
from V4 import RAGSystem, ConfigManager, UniversalResearchSpider

# Method 2: Root package import (new standard)
from viincci_rag import RAGSystem, ConfigManager, UniversalResearchSpider

# Method 3: Specific module import (future-proof)
from viincci_rag.core import RAGSystem, ConfigManager
from viincci_rag.core.spider import UniversalResearchSpider
```

### 3. **Resilient Import Fallbacks**

All wrappers use try/except to gracefully handle import failures:

```python
try:
    from V4.ConfigManager import ConfigManager
except Exception:  # pragma: no cover
    class ConfigManager:
        def __init__(self, *args, **kwargs):
            raise RuntimeError("ConfigManager is unavailable.")
```

This ensures the package never hard-crashes even if dependencies are missing.

## Migration Path

### Phase 1: ✅ **Backward Compatibility Layer** (COMPLETE)

- ✅ Created `viincci_rag` package with wrapper modules
- ✅ All imports from `V4` continue to work
- ✅ New imports from `viincci_rag` work identically
- ✅ Created test suite in `tests/` directory

### Phase 2: **Feature Parity** (NEXT)

Once all users have migrated to the new structure:

1. Move core logic from `V4/*.py` into `viincci_rag/core/`
2. Update `viincci_rag/core/__init__.py` to import from local modules
3. Keep `V4/` only for backward compatibility if needed

**Example after migration:**
```python
# viincci_rag/core/rag_system.py (after Phase 2)
# Contains full RAGSystem implementation, not a wrapper
class RAGSystem:
    def __init__(self, config=None):
        # Full implementation here
        pass
```

### Phase 3: **Deprecation** (OPTIONAL)

Once migration is complete, optionally:
- Add deprecation warnings to `V4` imports
- Provide migration guides to users
- Schedule removal of `V4` for major version bump

## How to Use

### For Existing Code (No Changes Required)

```python
# All V4 imports continue to work unchanged
from V4 import ConfigManager, RAGSystem, UniversalResearchSpider

config = ConfigManager(domain="botany")
rag = RAGSystem(config)
spider = UniversalResearchSpider(config)
```

### For New Code (Recommended)

```python
# Use the new viincci_rag package
from viincci_rag.core import ConfigManager, RAGSystem, UniversalResearchSpider

config = ConfigManager(domain="botany")
rag = RAGSystem(config)
spider = UniversalResearchSpider(config)
```

### For Tests

```python
# Tests use the new package structure
from viincci_rag.core import ConfigManager

def test_config():
    config = ConfigManager(verbose=False)
    assert config.get_current_domain() == "botany"
```

Run all tests:
```bash
pytest tests/
pytest tests/test_integration.py  # Test both import styles
```

## Package Layout Benefits

### ✅ Professional Structure
- Follows Python packaging standards (PEP 420, PEP 518)
- Ready for PyPI publication
- Installable via `pip install -e .`

### ✅ Future Modularization
- Easy to add subpackages (e.g., `viincci_rag.llm`, `viincci_rag.db`)
- Clear separation of concerns
- Easier testing and development

### ✅ Zero Breaking Changes
- Existing imports work unchanged
- Gradual migration path
- No rush to update code

### ✅ Better IDE Support
- Type hints work better with proper package structure
- IDE autocomplete improves
- Better support for documentation tools

## Files Modified/Created

### New Directories
- `viincci_rag/` - Main package
- `viincci_rag/core/` - Core modules
- `viincci_rag/database/` - Database adapters
- `viincci_rag/utils/` - Utilities
- `viincci_rag/config/` - Configuration
- `viincci_rag/templates/` - Templates
- `tests/` - Test suite

### New Files
- `viincci_rag/__init__.py` - Package root with re-exports
- `viincci_rag/core/__init__.py` - Core module initialization
- `viincci_rag/core/config.py` - ConfigManager wrapper
- `viincci_rag/core/rag_system.py` - RAGSystem wrapper
- `viincci_rag/core/spider.py` - Spider wrapper
- `viincci_rag/core/article_generator.py` - Article generator wrapper
- `viincci_rag/core/api_monitor.py` - API monitor wrapper
- `viincci_rag/database/__init__.py` - Database module
- `viincci_rag/utils/__init__.py` - Utils module
- `viincci_rag/templates/__init__.py` - Templates module
- `tests/__init__.py` - Test package
- `tests/test_config.py` - Config tests
- `tests/test_rag.py` - RAG tests
- `tests/test_spider.py` - Spider tests
- `tests/test_integration.py` - Integration tests

### Unchanged (Still Available)
- All `V4/` files remain unchanged
- Existing imports continue to work
- Configuration files in `V4/config/`
- Database files in `V4/db/`

## Testing

### Run All Tests
```bash
pytest tests/
```

### Run Specific Test Suite
```bash
pytest tests/test_config.py
pytest tests/test_rag.py
pytest tests/test_integration.py
```

### Test Coverage
```bash
pytest tests/ --cov=viincci_rag --cov-report=html
```

### Backward Compatibility Tests
The `test_integration.py` file specifically tests that all three import methods work:

```python
def test_backward_compatibility_v4_imports():
    """Test that V4 imports still work"""
    from V4 import ConfigManager, RAGSystem, UniversalResearchSpider
    # ...

def test_imports_from_viincci_rag_root():
    """Test that main classes can be imported from root package"""
    from viincci_rag import ConfigManager, RAGSystem
    # ...

def test_imports_from_viincci_rag_core():
    """Test that classes can be imported from viincci_rag.core"""
    from viincci_rag.core import ConfigManager, RAGSystem
    # ...
```

## Next Steps

1. **Run the test suite** to verify everything works:
   ```bash
   pytest tests/
   ```

2. **Update your imports** (optional, not required):
   - Old imports: `from V4 import ConfigManager` (still works)
   - New imports: `from viincci_rag.core import ConfigManager` (recommended)

3. **Future phases** (when ready):
   - Move core logic into `viincci_rag/core/`
   - Add additional subpackages as needed
   - Publish to PyPI

## FAQ

### Q: Do I need to update my code?
**A:** No! All existing imports continue to work. Update when you're ready or never if you prefer.

### Q: Will the V4 package be removed?
**A:** Not in the near future. It will remain for backward compatibility.

### Q: Can I use both import styles in the same project?
**A:** Yes! Both styles import the same underlying code, so there's no conflict.

### Q: How do I know which import to use?
**A:** For new code, prefer `from viincci_rag.core import ...` as it's the future standard. For existing code, no change is needed.

### Q: What about CLI entry points?
**A:** The CLI (`cli.py`, `research_cli.py`) can be exposed via `pyproject.toml` entry points after restructuring is complete.

## Summary

This restructuring achieves:
- ✅ Professional Python package structure
- ✅ Future-proof architecture
- ✅ **Zero breaking changes** (full backward compatibility)
- ✅ Clear migration path
- ✅ Ready for PyPI publication

Users can migrate at their own pace, with no urgency or breaking changes.
