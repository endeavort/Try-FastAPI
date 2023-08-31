# Try-fastAPI
## インストール
```ターミナル
-pip3 install -r requirements.txt
```

## 起動
```ターミナル
-cd app
-uvicorn main:app --reload 
```

## curlコマンド；HTTP GET リクエスト
### エンドポイント：ルート（/）
```ターミナル
-curl localhost:8000
```
### エンドポイント：/items/123
```ターミナル
-curl "localhost:8000/items/123"
```
### エンドポイント：/items/123 クエリ指定
```ターミナル
-curl "localhost:8000/items/123?q=hoge"
```

## curlコマンド；HTTP POST リクエスト
```ターミナル
-curl -X POST "http://localhost:8000/items" -H "Content-Type: application/json" -d "{\"name\":\"アイテム\",\"price\":123}"
```
-X POST: -X オプションを使用して、HTTPメソッドをPOSTに指定  
-H "Content-Type: application/json": リクエストヘッダーを指定。Content-Type ヘッダーを application/json に設定して、送信するデータが JSON 形式であることを指定している。  
-d "{\"name\":\"アイテム\",\"price\":123}": リクエストボディを指定。JSONオブジェクトを送信している。