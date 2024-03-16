# FletSample
Fletを使用したアプリ開発(Mac/Raspberry Pi)<br>
CPU温度を取得してそれをチャートに表示します。<br>
クリアボタンをクリックで、チャートをクリアします。<br>

## Macで開発
1. 作業ディレクトリ作成<br>
```sh
$ git clone https://github.com/taogya/FletSample.git
$ cd FletSample
```
2. 開発環境構築<br>
```sh
$ python3.9 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```
3. 実行<br>
GUIアプリとして起動<br>
```sh
$ cd src
$ python main.py
```
![demo](demo.gif)<br>

WEBアプリとして起動<br>
```sh
$ cd src
$ python main.py --host 0.0.0.0 --port 8080
```
http://localhost:8080<br>
