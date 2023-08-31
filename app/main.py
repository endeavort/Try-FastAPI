from fastapi import FastAPI
from pydantic import BaseModel

# FastAPIインスタンス
app = FastAPI()

# データの扱い設定
class Item(BaseModel):
    name: str
    price: float

# ルート（"/"）へのHTTP GETリクエストに対する処理を定義
@app.get("/")
async def root():
    # JSON形式に変換され、HTTPレスポンスの本文としてクライアントに返される
    return {"message": "Hello World"}

# /items/{item_id}へのHTTP GETリクエストに対する処理を定義
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# /items へのHTTP POSTリクエストに対する処理を定義
@app.post("/items")
def update_item(item: Item):
    return {"item_name": item.name, "twice price": item.price * 2}