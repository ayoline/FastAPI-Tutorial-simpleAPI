from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
banco = []


class Item(BaseModel):
    id: int
    quantidade: int
    descricao: str
    valor: float


@app.post("/item")
def add_item(item: Item):
    banco.append(item)
    return item


@app.get("/item")
def list_items():
    return banco


@app.get("/item/total")
def get_total():
    total = sum([item.quantidade * item.valor for item in banco])
    return {"valor total": total}
