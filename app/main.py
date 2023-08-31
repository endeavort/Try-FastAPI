from fastapi import FastAPI

# FastAPIインスタンス
app = FastAPI()

# ルート（"/"）へのHTTP GETリクエストに対する処理を定義
@app.get("/")
async def root():
    # JSON形式に変換され、HTTPレスポンスの本文としてクライアントに返される
    return {"message": "Hello World"}
