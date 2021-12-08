from fastapi import FastAPI
from pydantic import BaseModel
import pytest


app = FastAPI()

@app.get("/")
async def root():
    return {"mensagem" : "missao"}


class Resp(BaseModel):
    valor1: int
    valor2: int
    operacao: str

@app.post("/tarefa")
async def tarefa(resp: Resp):
    return resp

import pytest
from requests import get, post
from json import loads

class Teste:
    def setup(self):
        self.url = "http://127.0.0.1:8000"

    def test_APIstus(self):
        resp = get(self.url)
        assert resp.ok

    def test_APIreponse(self):
        resp = get(self.url)
        messi = loads(resp.text)
        assert messi["mensagem"] == "missao"
