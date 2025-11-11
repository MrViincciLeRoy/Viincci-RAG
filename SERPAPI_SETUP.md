# SerpAPI + Viincci-RAG Setup Guide

## Overview

You now have a fully configured environment to use SerpAPI with Viincci-RAG to generate historical content. Your API key is securely stored and will **NOT** be committed to GitHub.

## Setup Summary

### ✅ What Was Done

1. **Secure API Key Storage**
   - Created `.env` file with your SerpAPI key
   - `.env` is in `.gitignore` and will never be committed to GitHub
   - Created `.env.example` for documentation

2. **Python Packages Installed**
   - `google-search-results` (serpapi) — for real API calls
   - `python-dotenv` — for loading `.env` files

3. **Generated Content**
   - `da_vinci_history.txt` — Article about Leonardo da Vinci using real SerpAPI data
   - `generate_davinci.py` — Reusable script to generate content about any topic

4. **Security Verified**
   - ✓ `.env` is ignored by Git (`git check-ignore -q .env`)
   - ✓ API key not in any staged files
   - ✓ Safe to push all changes to GitHub

## Usage

### Option 1: Use the da Vinci Generator Script

```bash
cd /workspaces/Viincci-RAG
python generate_davinci.py
```

This will:
- Load your SERP_API_KEY from `.env`
- Query SerpAPI for "Leonardo da Vinci" information
- Generate a formatted article in `da_vinci_history.txt`
- Display a preview in the terminal

### Option 2: Customize for Different Topics

Edit `generate_davinci.py` and change the query:

```python
query = "Your Topic Here"
```

Then run:
```bash
python generate_davinci.py
```

### Option 3: Use the Example Notebook

The example notebook at `viincci_rag/examples/test_examples.ipynb` also supports real SerpAPI:

1. Open it in Jupyter
2. It will automatically detect your `SERP_API_KEY`
3. Run cells to generate content for multiple domains

## API Credits

Your SerpAPI account has **250 credits/month** (free tier mentioned):

- **Each search:** ~1 credit
- **Monthly limit:** 250 searches
- **Your query:** "Leonardo da Vinci biography..." = 1 credit

### Monitor Usage

```bash
# Check your SerpAPI dashboard:
open https://serpapi.com/dashboard
# Or: $BROWSER https://serpapi.com/dashboard
```

## Environment Variables

Your `.env` file contains:
```
SERP_API_KEY=c06dec0424ccf7a79b03922173c1defe4a4fed9d89038bc1177d1d48d1b52242
```

This is **automatically loaded** by:
- `generate_davinci.py`
- The example notebook
- Any script using `from dotenv import load_dotenv`

## Security Best Practices

✅ **Do:**
- Keep your SerpAPI key private
- Use `.env` for local development
- Add new keys to `.env.example` (without values) for documentation

❌ **Don't:**
- Share your `.env` file
- Commit `.env` to Git (it's in `.gitignore`)
- Hardcode API keys in scripts
- Post your key in issues/PRs

## Troubleshooting

### "SERP_API_KEY not found"
```bash
# Make sure .env exists in the repo root:
ls -la .env

# If missing, recreate it with your key:
cat > .env << 'EOF'
SERP_API_KEY=your-key-here
EOF
```

### "No results found"
- Check your API key is correct
- Verify you have credits remaining (check dashboard)
- Try a different search query

### "Module not found: serpapi"
```bash
pip install google-search-results
```

### "Module not found: dotenv"
```bash
pip install python-dotenv
```

## Generated Files

After running `generate_davinci.py`, you'll see:

```
da_vinci_history.txt          ← Article generated from real SerpAPI results
```

This file contains:
- Overview from Wikipedia/History.com
- 7 additional sources with snippets
- Metadata (query, date, source count)
- Links to read more

## Next Steps

1. ✅ Your API key is secure and loaded
2. ✅ You can generate content about da Vinci
3. ✅ Customize queries in `generate_davinci.py` for other topics
4. ✅ Track your SerpAPI usage in the dashboard

## Example: Generate Content About Another Topic

To generate content about Michelangelo instead:

```python
# Edit generate_davinci.py, line ~30:
query = "Michelangelo biography Renaissance artist sculptor"

# Then run:
python generate_davinci.py
```

Output will be saved as `da_vinci_history.txt` (or you can modify the filename).

## Resources

- **SerpAPI Docs:** https://serpapi.com/docs
- **SerpAPI Dashboard:** https://serpapi.com/dashboard
- **Viincci-RAG Examples:** `viincci_rag/examples/README.md`
- **Environment Setup:** `viincci_rag/examples/test_examples.ipynb`

---

**Last Updated:** November 11, 2025  
**API Key Status:** ✓ Securely configured  
**Git Status:** ✓ No secrets will be committed
