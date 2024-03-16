# FletSample
Fletを使用したアプリ開発(Mac/Raspberry Pi)<br>
CPU温度を取得してそれをチャートに表示します。<br>
クリアボタンをクリックで、チャートをクリアします。<br>

## Macで開発
1. 作業ディレクトリ作成
```sh
$ git clone git@github.com:taogya/FletSample.git
$ cd FletSample
```
2. 開発環境構築
```sh
$ python3.9 -m venv venv
$ . venv/bin/activate
$ pip install flet autopep8 isort flake8
$ pip freeze > requirements.txt
```
3. 実行
```sh
$ cd src
$ python main.py
```
![demo](demo.gif)