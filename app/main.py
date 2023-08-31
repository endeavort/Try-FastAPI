from fastapi import FastAPI

# FastAPIインスタンス
app = FastAPI()

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
