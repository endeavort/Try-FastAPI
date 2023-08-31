# Dockerイメージを指定
# tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim 
# FastAPIアプリケーションを動作させるための最小限の環境と、UvicornとGunicornというWebサーバーを含んでいる公式イメージ
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

# ホストマシン上の ./app ディレクトリ（Dockerfileと同じディレクトリ内にある app ディレクトリ）内のファイルを、
# Dockerコンテナ内の /app ディレクトリにコピーするための指示
COPY ./app /app