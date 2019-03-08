# dockerイメージを使ってNotebookサーバーを起動する方法

## 1. Docker Imageのビルド

`docker build ./ -t siva_handson`

## 2.Docker コンテナの起動

`docker run -it -p 8888:8888 siva_handson`