import re
from collections import Counter
from datetime import datetime, timezone

from dotenv import load_dotenv
from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

app = FastAPI()
client = OpenAI()


class EchoRequest(BaseModel):
    message: str


class EchoResponse(BaseModel):
    message: str
    timestamp: str


class AnalyseRequest(BaseModel):
    text: str


class AnalyseResponse(BaseModel):
    word_count: int
    top_words: list[tuple[str, int]]
    timestamp: str


class SummariseRequest(BaseModel):
    text: str


class SummariseResponse(BaseModel):
    summary: str
    timestamp: str


@app.get("/health")
def health_check():
    return {"status": "ok", "timestamp": datetime.now(timezone.utc).isoformat()}


@app.post("/echo")
def echo(request: EchoRequest) -> EchoResponse:
    return EchoResponse(
        message=request.message, timestamp=datetime.now(timezone.utc).isoformat()
    )


@app.post("/analyse")
def analyse(request: AnalyseRequest) -> AnalyseResponse:
    words = re.findall(r"\b[a-z]+\b", request.text.lower())
    count = Counter(words)
    return AnalyseResponse(
        word_count=len(words),
        top_words=count.most_common(5),
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


@app.post("/Summarise")
def summarise(request: SummariseRequest) -> SummariseResponse:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Summarise the following text concisely."},
            {"role": "user", "content": request.text},
        ],
    )
    summary = response.choices[0].message.content or ""
    return SummariseResponse(
        summary=summary, timestamp=datetime.now(timezone.utc).isoformat()
    )
