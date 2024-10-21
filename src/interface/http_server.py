# implement the http server with fastapi
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from adapter.openai import OpenAIClient
from app.answer_kb import AnswerKB
from domain.kb_item import Query
from repo.kbrepo import KBrepo

app = FastAPI()
kb_repo = KBrepo()
openai_client = OpenAIClient()

AnswerKB = AnswerKB(kb_repo, openai_client)


@app.get("/")
def read_root():
    return {"Hello World"}


# ask the bot a question
@app.post(
    "/assist/",
)
def assist(query: Query):
    answer = AnswerKB.execute(query, 3)
    return JSONResponse(content={"answer": answer})
