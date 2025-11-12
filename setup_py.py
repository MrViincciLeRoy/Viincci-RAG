#!/usr/bin/env python3
"""
setup.py - Package configuration for Viincci-RAG Research V4
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_file.exists():
    with open(requirements_file) as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="viincci-rag",
    version="4.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Universal multi-domain research system with RAG capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/viincci-rag",
    packages=find_packages(exclude=["tests", "tests.*", "docs", "_posts"]),
    include_package_data=True,
    package_data={
        "V4": [
            "config/*.json",
            "config/.gitkeep",
            "db/.gitkeep",
        ],
        "viincci_rag": [
            "config/*.json",
            "config/.gitkeep",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "pytest-mock>=3.11.0",
            "flake8>=6.1.0",
            "black>=23.0.0",
        ],
        "cuda": [
            "torch>=2.0.0",  # With CUDA support
        ],
    },
    entry_points={
        "console_scripts": [
            "viincci-research=V4.cli:main",
            "viincci-main=V4.main:main",
            "viincci-test=test_v4:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/viincci-rag/issues",
        "Source": "https://github.com/yourusername/viincci-rag",
        "Documentation": "https://github.com/yourusername/viincci-rag/wiki",
    },
)
