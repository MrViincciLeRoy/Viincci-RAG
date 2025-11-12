# Viincci-RAG

Universal multi-domain research system with RAG capabilities.

## Installation
```bash
pip install viincci-rag
```

## Quick Start
```python
from viincci_rag import ConfigManager, RAGSystem

# Initialize
config = ConfigManager()
rag = RAGSystem(config)
```

## Documentation
See full documentation at: https://github.com/viincci/Viincci-RAG

## License
MIT License - see LICENSE file for details.

## Maintainer
- **GitHub / PyPI Username**: MrViincciLeRoy
- **Email**: Viincci@proton.me

## ✨ Features

- 🔬 **Multi-Domain Research**: Botany, medical, mathematics, carpentry, and more
- 🤖 **RAG System**: Retrieval-Augmented Generation for intelligent answers
- � **Multiple Database Backends**: SQLite, PostgreSQL, MongoDB, MySQL
- 🎯 **API Monitoring**: Built-in SerpAPI credit tracking
- ⚙️ **Fully Configurable**: Models, databases, content processing
- ✅ **Tested & Documented**: Comprehensive test suite and documentation
- 🔄 **Backward Compatible**: All old imports still work

### Development Installation
```bash
# Clone the repository
git clone https://github.com/viincci/Viincci-RAG.git
cd Viincci-RAG

# Install in development mode
pip install -e .

# Or install with all dependencies
pip install -e ".[all]"
```

### For Development

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Or use the built-in test command
viincci-test
```

## 🔑 Setup

1. **Get a SerpAPI Key**: Sign up at [serpapi.com](https://serpapi.com/)

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

#### Basic Research Article
```bash
viincci-research -q "Rosa rubiginosa" -d botany
```

#### Plain Text Output
```bash
viincci-research -q "diabetes" -d medical --format text
```

#### JSON Structured Output
```bash
viincci-research -q "Pythagorean theorem" -d mathematics --format json
```

#### Arts & Humanities Research
```bash
viincci-research -q "Impressionism" -d art_history
viincci-research -q "Shakespeare sonnets" -d literature
```

#### Creative Writing with RAG
```bash
# Generate a poem
viincci-research -q "Van Gogh" -d art_history --content-type poem --rag

# Generate an essay
viincci-research -q "Baroque music" -d music --content-type essay --rag
```

#### Check API Status
```bash
viincci-research --check-credits
```

### Python API

```python
from V4 import ConfigManager, UniversalResearchSpider, RAGSystem, UniversalArticleGenerator

# Initialize configuration for a domain
config = ConfigManager(domain="mathematics", verbose=True)

# Perform research
spider = UniversalResearchSpider(config)
sources = spider.research("Pythagorean theorem")

# Generate article with RAG
rag = RAGSystem(config)
texts = [s['text'] for s in sources]
metadata = [s['metadata'] for s in sources]
rag.build_index(texts, metadata)
rag.load_llm()

generator = UniversalArticleGenerator(config, rag_system=rag)
article = generator.generate_full_article("Pythagorean theorem", sources)

# Save article
with open("article.html", "w") as f:
    f.write(article)
```

### Domain Information

```bash
# List all domains
viincci-research --list-domains

# Get detailed domain info
viincci-research --domain-info medical
```

## 🏗️ Architecture

```
viincci-rag/
├── V4/                          # Main package
│   ├── __init__.py             # Package exports
│   ├── ConfigManager.py        # Configuration management
│   ├── Spider.py               # Web scraping & search
│   ├── RagSys.py              # RAG system implementation
│   ├── UniversalArticleGenerator.py  # Article generation
│   ├── ApiMonitor.py          # API credit monitoring
│   ├── FloraDatabase.py       # Database operations
│   ├── config/                # Configuration files
│   │   ├── domains.json       # Domain definitions
│   │   ├── ai_settings.json   # AI model settings
│   │   ├── api_monitor.json   # API monitoring config
│   │   └── ...
│   └── db/                    # Database directory
├── research_cli.py            # Command-line interface
├── test_v4.py                # Test suite
├── requirements.txt          # Dependencies
├── setup.py                  # Package setup
└── README.md                 # This file
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Using pytest
pytest

# Using built-in test runner
viincci-test

# With verbose output
viincci-test --verbose

# Run specific test
pytest tests/test_config.py -v
```

## 📊 Configuration

All configuration is stored in `V4/config/` as JSON files:

- **domains.json**: Define research domains, sources, questions
- **ai_settings.json**: LLM and embedding model settings
- **api_monitor.json**: API usage thresholds and alerts
- **search_config.json**: Web scraping parameters
- **domain_reliability.json**: Source reliability scores

### Example: Add a New Domain

Edit `V4/config/domains.json`:

```json
{
  "your_domain": {
    "name": "Your Domain Name",
    "description": "Description of your domain",
    "primary_sources": ["university", "research_institute"],
    "questions": [
      "what are the key concepts",
      "what are the applications"
    ],
    "keywords": ["keyword1", "keyword2"]
  }
}
```

## 🔧 Advanced Features

### RAG System Customization

```python
from V4 import ConfigManager, RAGSystem

config = ConfigManager()

# Change LLM model
config.set_llm_model("LiquidAI/LFM-40B-MoE")

# Initialize RAG with custom settings
rag = RAGSystem(config)
rag.load_llm(device="cuda", load_in_8bit=True)

# Query with custom parameters
result = rag.query(
    "What are the benefits?",
    k=10,
    max_new_tokens=500,
    temperature=0.8
)
```

### API Cost Estimation

```python
from V4 import SerpAPIMonitor, ConfigManager

config = ConfigManager()
monitor = SerpAPIMonitor(config)

# Estimate research cost
estimate = monitor.estimate_research_cost("Plant name", questions=4)
monitor.print_estimate(estimate)

# Check if can afford
if estimate['can_afford']:
    # Proceed with research
    pass
```

## 📚 Documentation

For detailed documentation, visit: https://github.com/viincci/Viincci-RAG

### Key Topics

- [Installation Guide](https://github.com/viincci/Viincci-RAG)
- [Configuration Reference](https://github.com/viincci/Viincci-RAG)
- [API Documentation](https://github.com/viincci/Viincci-RAG)
- [Domain Creation Guide](https://github.com/viincci/Viincci-RAG)
- [RAG System Guide](https://github.com/viincci/Viincci-RAG)

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) first.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [SerpAPI](https://serpapi.com/) for search capabilities
- [Hugging Face](https://huggingface.co/) for transformers and models
- [FAISS](https://github.com/facebookresearch/faiss) for efficient similarity search
- [Wikimedia Commons](https://commons.wikimedia.org/) for images

## 📞 Support

- 📧 Email: Viincci@proton.me
- GitHub: [MrViincciLeRoy](https://github.com/MrViincciLeRoy)
- 🐛 Issues: [GitHub Issues](https://github.com/viincci/Viincci-RAG/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/viincci/Viincci-RAG/discussions)

## 🗺️ Roadmap

- [ ] Add more research domains
- [ ] Implement caching for search results
- [ ] Add web interface
- [ ] Support for more LLM providers
- [ ] Multilingual support
- [ ] Export to more formats (PDF, DOCX)
- [ ] Integration with reference managers

## 📈 Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

**Made with ❤️ by the Viincci-RAG Team**
