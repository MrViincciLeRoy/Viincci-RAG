# Viincci-RAG

> Universal multi-domain research system with RAG (Retrieval-Augmented Generation) capabilities

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://img.shields.io/pypi/v/viincci-rag.svg)](https://pypi.org/project/viincci-rag/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/viincci-rag)](https://pepy.tech/project/viincci-rag)
[![Status: Beta](https://img.shields.io/badge/Status-Beta-orange.svg)]()

**Viincci-RAG** is a powerful, flexible research assistant that combines web scraping, intelligent document retrieval, and AI-powered content generation. Built for researchers, content creators, and domain experts who need comprehensive, well-sourced information on any topic.

## ✨ Key Features

- 🔬 **Multi-Domain Research**: Supports botany, medical, mathematics, carpentry, art, literature, and more
- 🤖 **Advanced RAG System**: Retrieval-Augmented Generation for accurate, context-aware responses
- 🗄️ **Multiple Database Backends**: SQLite, PostgreSQL, MongoDB, MySQL support
- 🎯 **API Cost Management**: Built-in SerpAPI credit tracking and estimation
- ⚙️ **Fully Configurable**: Customize models, databases, output formats, and content processing
- 📊 **Rich Output Formats**: HTML articles, plain text, JSON, and more
- 🧪 **Tested & Documented**: Comprehensive test suite with 95%+ coverage
- 🔄 **Backward Compatible**: All legacy imports continue to work seamlessly

## 🚀 Quick Start

### Installation from PyPI

```bash
# Basic installation
pip install viincci-rag

# With all dependencies
pip install viincci-rag[all]

# For development
pip install viincci-rag[dev]
```

### Installation from Source

```bash
# Clone and install
git clone https://github.com/MrViincciLeRoy/Viincci-RAG.git
cd Viincci-RAG
pip install -e .
```

### 🎓 Try It Now (No Installation Required!)

Run these interactive notebooks in your browser:

- [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MrViincciLeRoy/Viincci-RAG/blob/main/viincci_rag/examples/test_examples.ipynb) **Minimal Examples** — Safe mock mode + real SerpAPI integration
- [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MrViincciLeRoy/Viincci-RAG/blob/main/Test.ipynb) **Complete Testing** — All domains (poetry, medical, botany, art, carpentry)

## 🔑 Setup

1. **Get a SerpAPI Key** (required for web search):
   - Sign up at [serpapi.com](https://serpapi.com/)
   - Free tier includes 100 searches/month

2. **Set Environment Variable**:
   ```bash
   export SERP_API_KEY='your_api_key_here'
   ```

3. **Verify Installation**:
   ```bash
   viincci-research --list-domains
   ```

## 📖 Usage

### Command Line Interface

```bash
# Basic research article
viincci-research -q "Rosa rubiginosa" -d botany

# Medical research with plain text output
viincci-research -q "diabetes treatment" -d medical --format text

# Mathematical concepts in JSON format
viincci-research -q "Pythagorean theorem" -d mathematics --format json

# Arts & humanities research
viincci-research -q "Impressionism" -d art_history
viincci-research -q "Shakespeare sonnets" -d literature

# Creative writing with RAG
viincci-research -q "Van Gogh" -d art_history --content-type poem --rag
viincci-research -q "Baroque music" -d music --content-type essay --rag

# Check API credits
viincci-research --check-credits
```

### Python API

```python
from viincci_rag import ConfigManager, RAGSystem, UniversalResearchSpider

# Initialize configuration
config = ConfigManager(domain="mathematics", verbose=True)

# Create RAG system
rag = RAGSystem(config)
rag.load_llm()

# Create research spider
spider = UniversalResearchSpider(config)

# Perform research
sources = spider.research("Pythagorean theorem")

# Generate article with RAG
texts = [s['text'] for s in sources]
metadata = [s['metadata'] for s in sources]
rag.build_index(texts, metadata)

# Query the system
answer = rag.query("What is the Pythagorean theorem?")
print(answer)
```

### Simple Example

```python
from viincci_rag import *

# Quick start - just research and generate
config = ConfigManager(domain="botany")
spider = UniversalResearchSpider(config)
sources = spider.research("Rosa rubiginosa")

# Generate article
rag = RAGSystem(config)
rag.load_llm()
generator = UniversalArticleGenerator(config, rag_system=rag)
article = generator.generate_full_article("Rosa rubiginosa", sources)

# Save to file
with open("article.html", "w") as f:
    f.write(article)
```

## 📦 What's Included

| Component | Purpose |
|-----------|---------|
| `ConfigManager` | Configuration management with domain support |
| `RAGSystem` | Retrieval-Augmented Generation pipeline |
| `UniversalResearchSpider` | Multi-domain web scraping and research |
| `UniversalArticleGenerator` | AI-powered content generation |
| `SerpAPIMonitor` | API credit monitoring and cost estimation |
| `FloraDatabase` | Database operations and management |

## 🏗️ Architecture

```
viincci-rag/
├── viincci_rag/           # Main package
│   ├── core/              # Core RAG modules
│   ├── database/          # Database adapters
│   ├── utils/             # Utility functions
│   ├── config/            # Configuration files
│   └── templates/         # Output templates
├── V4/                    # Original codebase (backward compatible)
├── docs/                  # Documentation
├── tests/                 # Test suite
└── examples/              # Usage examples
```

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=viincci_rag --cov-report=html

# Run integration tests
pytest tests/test_integration.py -v

# Use built-in test command
viincci-test
```

## 📊 Supported Domains

- 🌿 **Botany** - Plant research and taxonomy
- ⚕️ **Medical** - Healthcare and medical research
- 🔢 **Mathematics** - Mathematical concepts and proofs
- 🔨 **Carpentry** - Woodworking and construction
- 🎨 **Art History** - Visual arts and movements
- 📚 **Literature** - Literary analysis and criticism
- 🎵 **Music** - Music theory and history
- 🏛️ **History** - Historical events and periods
- 🔬 **Science** - General scientific research
- 💻 **Technology** - Computing and engineering

```bash
# List all available domains
viincci-research --list-domains

# Get detailed info about a domain
viincci-research --domain-info medical
```

## 🔧 Advanced Features

### Custom LLM Configuration

```python
from viincci_rag import ConfigManager, RAGSystem

config = ConfigManager()

# Change LLM model
config.set_llm_model("LiquidAI/LFM-40B-MoE")

# Initialize with custom settings
rag = RAGSystem(config)
rag.load_llm(device="cuda", load_in_8bit=True)

# Query with parameters
result = rag.query(
    "What are the benefits?",
    k=10,
    max_new_tokens=500,
    temperature=0.8
)
```

### API Cost Estimation

```python
from viincci_rag import SerpAPIMonitor, ConfigManager

config = ConfigManager()
monitor = SerpAPIMonitor(config)

# Estimate research cost
estimate = monitor.estimate_research_cost("Plant name", questions=4)
monitor.print_estimate(estimate)

# Check if affordable
if estimate['can_afford']:
    # Proceed with research
    pass
```

### Database Configuration

```python
from viincci_rag import ConfigManager

# SQLite (default)
config = ConfigManager(db_type="sqlite")

# PostgreSQL
config = ConfigManager(
    db_type="postgresql",
    db_config={
        "host": "localhost",
        "port": 5432,
        "database": "mydb",
        "user": "user",
        "password": "pass"
    }
)

# MongoDB
config = ConfigManager(
    db_type="mongodb",
    db_config={
        "host": "localhost",
        "port": 27017,
        "database": "mydb"
    }
)
```

## 📚 Documentation

Complete documentation is available in the `docs/` folder:

- **[docs/DOCS.md](docs/DOCS.md)** - Documentation index and quick reference
- **[docs/MIGRATION.md](docs/MIGRATION.md)** - Migration guide from V3 to V4
- **[docs/RESTRUCTURING_SUMMARY.md](docs/RESTRUCTURING_SUMMARY.md)** - Architecture overview
- **[docs/BACKWARD_COMPATIBILITY_SHIMS.md](docs/BACKWARD_COMPATIBILITY_SHIMS.md)** - Compatibility details
- **[docs/package_structure.md](docs/package_structure.md)** - Package structure guide

## 🔄 Backward Compatibility

All old imports continue to work seamlessly:

```python
# Old import (still works)
from V4 import ConfigManager, RAGSystem

# New import (recommended)
from viincci_rag import ConfigManager, RAGSystem

# Both are identical
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Run tests: `pytest tests/`
5. Submit a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 🗺️ Roadmap

- [ ] Additional research domains (chemistry, geography, etc.)
- [ ] Web interface with REST API
- [ ] Caching system for search results
- [ ] Support for more LLM providers (Anthropic, Cohere, etc.)
- [ ] Multilingual support
- [ ] PDF and DOCX export formats
- [ ] Integration with reference managers (Zotero, Mendeley)
- [ ] Real-time collaborative research features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [SerpAPI](https://serpapi.com/) for search capabilities
- [Hugging Face](https://huggingface.co/) for transformers and models
- [FAISS](https://github.com/facebookresearch/faiss) for efficient similarity search
- [Wikimedia Commons](https://commons.wikimedia.org/) for educational resources

## 📞 Support

- 📧 **Email**: Viincci@proton.me
- 🐛 **Issues**: [GitHub Issues](https://github.com/MrViincciLeRoy/Viincci-RAG/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/MrViincciLeRoy/Viincci-RAG/discussions)
- 👤 **GitHub**: [@MrViincciLeRoy](https://github.com/MrViincciLeRoy)

## 📈 Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and release notes.

## Citation

If you use Viincci-RAG in your research or project, please cite:

```bibtex
@software{viincci_rag_2024,
  author = {Viincci},
  title = {Viincci-RAG: Universal Multi-Domain Research System with RAG},
  year = {2024},
  url = {https://github.com/MrViincciLeRoy/Viincci-RAG},
  version = {4.0.0}
}
```

---

**Version**: 4.0.0 | **Status**: Beta | **License**: MIT

**Made with ❤️ by the Viincci-RAG Team**
