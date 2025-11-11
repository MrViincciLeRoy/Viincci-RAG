# Viincci-RAG Examples

This directory contains safe, reusable examples for the Viincci-RAG package with backwards-compatible import logic and SerpAPI cost management.

## Files

- `test_examples.ipynb` — A minimal notebook that demonstrates:
  - **Backwards-compatible imports** that prefer `viincci_rag` (new layout) and fall back to `V4` (legacy)
  - **SerpAPI mock** to avoid consuming free SerpAPI credits while iterating locally
  - **Safe generation** with fallback outputs when the real library is not available

## Quick Start

### Using the Mock (No SerpAPI Credits Required)

The notebook uses a **deterministic mock SerpAPI client** by default. This is perfect for:
- Learning how the library works
- Testing your prompts and generation code
- Iterating without spending SerpAPI credits (250/month free tier)

Simply open `test_examples.ipynb` and run the cells. The mock will return example search results, and the notebook will either:
1. Use the real generators (if `viincci_rag` is installed) to create content, or
2. Write safe fallback `.txt` files with stitched search results

### Using Real SerpAPI (Optional)

To use your real SerpAPI credentials:

1. Set the environment variable:
   ```bash
   export SERP_API_KEY="your-key-here"
   ```

2. Ensure the `serpapi` package is installed:
   ```bash
   pip install google-search-results
   ```

3. Run the notebook again. The cells will prefer the real SerpAPI client if the key is set and the package is available.

## Import Compatibility

The notebook uses a smart import fallback strategy:

```python
def try_import():
    try:
        # Prefer the new viincci_rag layout
        from viincci_rag.core.config import ConfigManager
        ...
    except:
        # Fall back to legacy V4 package
        from V4 import ConfigManager
        ...
```

This ensures that whether you have the new `viincci_rag` package installed or the older `V4` version, the examples will work.

## Domains Supported

The example uses domains like:
- `botany` — Plant research and articles
- `literature` — Poetry and literary content
- `carpentry` — Technical guides and tutorials

The mock will generate plausible "research results" for any query, making it safe to iterate on your generation logic.

## Output Files

After running the notebook, you'll see files like:
- `fallback_botany.txt`
- `fallback_literature.txt`
- `fallback_carpentry.txt`

These contain either real generated content (if the full library is available) or safe fallback summaries of mock search results.

## Testing

To verify the examples work correctly:

```bash
pytest tests/test_examples.py -v
```

This runs 6 tests that validate:
1. Backwards-compatible import logic
2. Mock SerpAPI returns expected results
3. Search result normalization
4. Fallback file generation
5. Notebook validity (nbformat v4+)
6. `Test.ipynb` widget metadata is correct

## Tips

- **Save SerpAPI credits**: Use the mock by default; only enable real SerpAPI when you're ready to test with live data.
- **Iterate safely**: The fallback outputs are deterministic, so you can test generation without randomness from real web searches.
- **Check domain config**: See `V4/config/domains.json` or `viincci_rag/config/` for available domains and their settings.
- **Customize content**: Modify the `content_type` and `format` parameters in generation calls to produce different outputs (poems, essays, HTML, etc.).

## References

- [viincci_rag package](../README.md)
- [Backwards compatibility docs](../docs/BACKWARD_COMPATIBILITY_SHIMS.md)
- [SerpAPI pricing](https://serpapi.com/pricing)
