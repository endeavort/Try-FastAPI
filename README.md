# Try-fastAPI
## インストール
pip3 install -r requirements.txt

## 起動
cd app
uvicorn main:app --reload 

## curlコマンド；HTTP GET リクエスト
### エンドポイント：ルート（/）
curl localhost:8000
### エンドポイント：/items/123
curl "localhost:8000/items/123"
### エンドポイント：/items/123 クエリ指定
curl "localhost:8000/items/123?q=hoge"

## curlコマンド；HTTP POST リクエスト
curl -X POST "http://localhost:8000/items" -H "Content-Type: application/json" -d "{\"name\":\"おなまえ\",\"price\":123}"
{"item_name":"おなまえ","twice price":246.0}