# Backward Compatibility Shims Reference

This document lists all the compatibility wrappers created to ensure zero breaking changes.

## How Backward Compatibility Works

Each module in `viincci_rag.core/` is a **thin wrapper** that:

1. Attempts to import from the legacy `V4/` package
2. Re-exports the imported class/function
3. Falls back to a stub if import fails
4. Is resilient to missing dependencies

## Wrapper Modules

### 1. `viincci_rag/core/config.py`
**Wraps**: `V4.ConfigManager.ConfigManager`
**Purpose**: Configuration management with domain support
**Import Paths**:
- `from V4 import ConfigManager`
- `from viincci_rag import ConfigManager` 
- `from viincci_rag.core import ConfigManager`
- `from viincci_rag.core.config import ConfigManager`

### 2. `viincci_rag/core/rag_system.py`
**Wraps**: `V4.RagSys.RAGSystem`
**Purpose**: RAG (Retrieval-Augmented Generation) system
**Import Paths**:
- `from V4 import RAGSystem`
- `from viincci_rag import RAGSystem`
- `from viincci_rag.core import RAGSystem`
- `from viincci_rag.core.rag_system import RAGSystem`

### 3. `viincci_rag/core/spider.py`
**Wraps**: `V4.Spider.UniversalResearchSpider`
**Purpose**: Multi-domain research spider with API monitoring
**Import Paths**:
- `from V4 import UniversalResearchSpider`
- `from viincci_rag import UniversalResearchSpider`
- `from viincci_rag.core import UniversalResearchSpider`
- `from viincci_rag.core.spider import UniversalResearchSpider`

### 4. `viincci_rag/core/article_generator.py`
**Wraps**: `V4.UniversalArticleGenerator.UniversalArticleGenerator`
**Purpose**: Domain-agnostic article generation
**Import Paths**:
- `from V4 import UniversalArticleGenerator`
- `from viincci_rag import UniversalArticleGenerator`
- `from viincci_rag.core import UniversalArticleGenerator`
- `from viincci_rag.core.article_generator import UniversalArticleGenerator`

### 5. `viincci_rag/core/api_monitor.py`
**Wraps**: `V4.ApiMonitor.SerpAPIMonitor`
**Purpose**: SerpAPI credit monitoring and management
**Import Paths**:
- `from V4 import SerpAPIMonitor`
- `from viincci_rag import SerpAPIMonitor`
- `from viincci_rag.core import SerpAPIMonitor`
- `from viincci_rag.core.api_monitor import SerpAPIMonitor`

### 6. `viincci_rag/database/__init__.py`
**Wraps**: `V4.FloraDatabase.FloraDatabase`
**Purpose**: Database operations
**Import Paths**:
- `from V4 import FloraDatabase`
- `from viincci_rag import FloraDatabase`
- `from viincci_rag.database import FloraDatabase`

## Compatibility Matrix

| Import Style | Works | Status | Recommended For |
|---|---|---|---|
| `from V4 import X` | ✅ Yes | Stable | Existing code |
| `from viincci_rag import X` | ✅ Yes | Recommended | New code |
| `from viincci_rag.core import X` | ✅ Yes | Future-proof | New imports |
| `from viincci_rag.core.X import Y` | ✅ Yes | Specific | Direct imports |

## Testing

All backward compatibility has been tested and verified:

```bash
pytest tests/test_integration.py -v
```

**Results**: ✅ 3/3 integration tests passing

---

**See also**: `MIGRATION.md` for comprehensive guide | `RESTRUCTURING_SUMMARY.md` for summary
