#!/usr/bin/env python3
"""
Lightweight remote generator for a small "DocumentArray" JSON using an OpenAI-style API.

Usage (recommended):
  - Save your API key into the repository secrets as `OPENAI_API_KEY` (do NOT commit keys).
  - Trigger the workflow `.github/workflows/remote-test.yml` (workflow_dispatch) or run locally with:
      OPENAI_API_KEY="<key>" python tools/generate_da.py

This script purposely keeps the request small and the output small to avoid heavy downloads.
"""
import os
import sys
import json
import requests
from datetime import datetime


def main():
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY not set. Set it in environment or GitHub Secrets.")
        sys.exit(2)

    endpoint = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Small prompt to avoid large responses
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": (
                "Write a short (40-80 word) neutral description of the project named 'Viincci-RAG'."
                " Return only plain text as the assistant message."
            ),
        },
    ]

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "max_tokens": 200,
        "temperature": 0.2,
    }

    try:
        resp = requests.post(endpoint, headers=headers, json=payload, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        print("ERROR: API request failed:", e)
        if resp is not None and getattr(resp, 'content', None):
            try:
                print("Response:", resp.content.decode())
            except Exception:
                pass
        sys.exit(3)

    data = resp.json()
    try:
        text = data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("ERROR: Unexpected API response format:", e)
        print(json.dumps(data, indent=2))
        sys.exit(4)

    doc = {
        "text": text,
        "metadata": {
            "source": "openai",
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "model": payload["model"],
        },
    }

    outdir = os.path.join(os.getcwd(), "output")
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, "da.json")
    with open(outpath, "w", encoding="utf-8") as f:
        json.dump([doc], f, ensure_ascii=False, indent=2)

    print(f"Wrote DocumentArray-like JSON to {outpath}")
    print("--- sample ---")
    print(text)


if __name__ == "__main__":
    main()
