# Gemini API Python Project

A simple Python project for calling Google Gemini models and building a basic CLI chatbot.

## Project Structure

- `config.py` – Loads environment variables (including `GEMINI_API_KEY`) from `.env`.
- `gemini_client.py` – Example script that sends one prompt to Gemini and prints the response.
- `main.py` – Chat loop entry point (expects `services/ai_service.py` to provide `ask_gemini`).

## Requirements

- Python 3.9+
- A Gemini API key

## Install

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install google-genai python-dotenv
```

## Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

## Run

### 1) Run the simple API example

```bash
python gemini_client.py
```

### 2) Run chatbot loop

```bash
python main.py
```

## Important Notes

- Do **not** commit API keys to source control.
- If `main.py` fails with `ModuleNotFoundError: No module named 'services'`, create `services/ai_service.py` (or update imports) so `ask_gemini()` is available.
- Consider updating `gemini_client.py` to read the key from environment variables instead of hardcoding it.

## Suggested Next Improvement

Refactor all Gemini calls to use a single client setup that reads from `GEMINI_API_KEY` in `config.py`.
