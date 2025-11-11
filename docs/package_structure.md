# Complete Package Structure & Build Guide

## 📁 Final Directory Structure

```
viincci-rag/
├── V4/                              # Main package
│   ├── __init__.py                 # Package exports
│   ├── ConfigManager.py
│   ├── Spider.py
│   ├── RagSys.py
│   ├── UniversalArticleGenerator.py
│   ├── ArtGenSys.py
│   ├── ApiMonitor.py
│   ├── FloraDatabase.py
│   ├── FloraWikipediaScraper.py
│   ├── config/                     # Configuration files
│   │   ├── .gitkeep
│   │   ├── ai_settings.json
│   │   ├── api_monitor.json
│   │   ├── article_config.json
│   │   ├── config.json
│   │   ├── domain_reliability.json
│   │   ├── domains.json
│   │   └── search_config.json
│   └── db/                         # Database directory
│       └── .gitkeep
├── tests/                          # Test directory
│   ├── __init__.py
│   ├── test_config.py
│   ├── test_spider.py
│   ├── test_rag.py
│   └── test_integration.py
├── docs/                           # Documentation
│   ├── index.md
│   ├── installation.md
│   ├── usage.md
│   └── api.md
├── .github/                        # GitHub workflows
│   └── workflows/
│       ├── test.yml
│       ├── test-cli.yml
│       └── serp-api.yml
├── research_cli.py                 # CLI entry point
├── test_v4.py                     # Legacy test runner
├── setup.py                        # Package setup (legacy)
├── pyproject.toml                 # Modern package config
├── MANIFEST.in                    # Package manifest
├── requirements.txt               # Dependencies
├── requirements-dev.txt           # Dev dependencies
├── README.md                      # Main documentation
├── CHANGELOG.md                   # Version history
├── LICENSE                        # License file
├── CONTRIBUTING.md                # Contribution guidelines
├── .gitignore                     # Git ignore rules
└── .flake8                        # Linter config
```

## 🔨 Building the Package

### 1. Create Additional Required Files

#### requirements-dev.txt
```txt
# Development dependencies
pytest>=7.4.0
pytest-cov>=4.1.0
pytest-mock>=3.11.0
flake8>=6.1.0
black>=23.0.0
isort>=5.12.0
mypy>=1.5.0

# Documentation
sphinx>=7.0.0
sphinx-rtd-theme>=1.3.0

# Build tools
build>=0.10.0
twine>=4.0.0
wheel>=0.41.0
```

#### CHANGELOG.md
```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [4.0.0] - 2024-01-XX

### Added
- Universal multi-domain research system
- Support for 12 research domains
- RAG-powered content generation
- Multiple output formats (HTML, Text, JSON)
- Creative writing capabilities (poems, essays)
- API credit monitoring
- Comprehensive test suite
- CLI interface

### Changed
- Migrated from domain-specific to universal architecture
- Improved configuration management
- Enhanced error handling

### Fixed
- Various bug fixes and improvements

## [3.0.0] - Previous versions
...
```

#### LICENSE
```txt
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

#### .gitignore
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
venv/
ENV/
env/
.venv

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Testing
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/
htmlcov/

# Database
*.db
*.sqlite
*.sqlite3

# Research outputs
_posts/*.html
_posts/*.txt
_posts/*.json
research_output/

# Logs
*.log

# Environment
.env
.env.local
```

### 2. Build Commands

```bash
# Install build tools
pip install build twine wheel

# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build the package
python -m build

# This creates:
# - dist/viincci_rag-4.0.0-py3-none-any.whl (wheel)
# - dist/viincci-rag-4.0.0.tar.gz (source)
```

### 3. Test the Built Package

```bash
# Create a test virtual environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install the wheel
pip install dist/viincci_rag-4.0.0-py3-none-any.whl

# Test installation
viincci-research --list-domains
viincci-test

# Deactivate when done
deactivate
```

### 4. Publish to PyPI

#### Test PyPI (Recommended First)
```bash
# Upload to Test PyPI
python -m twine upload --repository testpypi dist/*

# Install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ viincci-rag

# Test it works
viincci-research --list-domains
```

#### Production PyPI
```bash
# Upload to PyPI
python -m twine upload dist/*

# Install from PyPI
pip install viincci-rag
```

### 5. Development Installation

```bash
# Clone repository
git clone https://github.com/yourusername/viincci-rag.git
cd viincci-rag

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run linter
flake8 V4/

# Format code
black V4/

# Sort imports
isort V4/
```

## 📦 Package Verification Checklist

Before publishing, verify:

- [ ] All tests pass: `pytest`
- [ ] CLI works: `viincci-research --list-domains`
- [ ] Package builds: `python -m build`
- [ ] Wheel installs: `pip install dist/*.whl`
- [ ] README renders correctly on PyPI
- [ ] Version number is correct in all files
- [ ] CHANGELOG is updated
- [ ] LICENSE file exists
- [ ] All dependencies are listed
- [ ] Config files are included in package
- [ ] Entry points work correctly

## 🚀 Quick Start for Users

After publishing to PyPI, users can:

```bash
# Install
pip install viincci-rag

# Set API key
export SERP_API_KEY='your_key'

# Run research
viincci-research -q "Rosa rubiginosa" -d botany

# Check help
viincci-research --help
```

## 🔄 Version Management

Update version in these files:
1. `setup.py` (line 25)
2. `pyproject.toml` (line 7)
3. `V4/__init__.py` (__version__)
4. `CHANGELOG.md`

## 📚 Additional Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [PyPI Publishing Tutorial](https://packaging.python.org/tutorials/packaging-projects/)
- [Setuptools Documentation](https://setuptools.pypa.io/)
- [Poetry Documentation](https://python-poetry.org/) (alternative to setuptools)
