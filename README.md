# Try-fastAPI
FastAPIを初めて利用して作成

## インストール
```ターミナル
pip3 install -r requirements.txt
```

## 起動
```ターミナル
cd app
uvicorn main:app --reload 
```

## curlコマンド；HTTP GET リクエスト
### エンドポイント：ルート（/）
```ターミナル
curl localhost:8000
```
### エンドポイント：/items/123
```ターミナル
curl "localhost:8000/items/123"
```
### エンドポイント：/items/123 クエリ指定
```ターミナル
curl "localhost:8000/items/123?q=hoge"
```

## curlコマンド；HTTP POST リクエスト
```ターミナル
curl -X POST "http://localhost:8000/items" -H "Content-Type: application/json" -d "{\"name\":\"アイテム\",\"price\":123}"
```
#### -X POST
-X オプションを使用して、HTTPメソッドをPOSTに指定  
#### -H "Content-Type: application/json"
リクエストヘッダーを指定。Content-Type ヘッダーを application/json に設定して、送信するデータが JSON 形式であることを指定している。  
#### -d "{\"name\":\"アイテム\",\"price\":123}"
リクエストボディを指定。JSONオブジェクトを送信している。

## docker
### imageをbuild
```ターミナル
docker build -t sample-api:1.0.0 .
```
#### -t sample-api:1.0.0
-t オプションは、ビルドされるイメージにタグ（Tag）を付ける。イメージ名とタグは任意で、イメージを識別するために使用。  
イメージ名：sample-api  
タグ：1.0.0  
#### "."
最後の"."はカレントディレクトリを表す。このディレクトリ内に Dockerfile が存在し、それを使用して Docker イメージがビルドされる。

### コンテナを実行
```ターミナル
docker run -d --name sample-api-container -p 80:80 sample-api:1.0.0
```
#### -d
-d オプションはコンテナをデタッチドモード（バックグラウンドモード）で実行
#### --name sample-api-container
コンテナの名前は「sample-api-container」となる
#### -p 80:80 
ホストのポート80を介してコンテナのポート80にアクセスできるようになる
#### sample-api:1.0.0
実行するコンテナのイメージを指定

### コンテナの外からcurlを打つ
```ターミナル
curl localhost:80
```

### コンテナをストップ
```ターミナル
docker stop sample-api-container
```

### コンテナを削除
```ターミナル
docker rm sample-api-container
```

### imageを削除
```ターミナル
docker image rm sample-api:1.0.0
```
