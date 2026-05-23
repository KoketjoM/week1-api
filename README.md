# Week 1 API

A FastAPI application built as part of the Applied AI Engineer bootcamp.

## Endpoints

| Method | Path | Description |
| -------- | ------ | ------------- |
| GET | `/health` | Returns API status and timestamp |
| POST | `/echo` | Accepts a message and returns it with a timestamp |
| POST | `/analyse` | Returns word count and top 5 words from input text |
| POST | `/summarise` | Summarises input text using OpenAI |

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/week1-api.git
cd week1-api
C:\Python312\python.exe -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the root directory:

```bash
OPENAI_API_KEY=your_key_here
```

## Running

```bash
uvicorn app.main:app --reload
```

Then open `http://127.0.0.1:8000/docs` to test the endpoints.

## Tech Stack

- Python 3.12
- FastAPI
- Pydantic
- OpenAI API

