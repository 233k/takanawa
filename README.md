# takanawa

Slack の Outgoing Webhook と Incoming Webhook でメッセージを転送するよ

## Installation

### slack
#### Incoming webhook 設定
- 流したいチャンネルに設定する
- URL を控えておく

#### Outgoing webhook 設定
- 対象のチャンネルを設定する
- 引き金となる言葉に送信先の workspace を設定する
- このアプリが動くサーバのうｒｌを設定する

### app
python3

#### コンフィグ
config.py の WORKSPACES_AND_WEB_HOOK_DICT を
workspace名 : そのワークスペースのIncomingHookURL の形式で追加する

#### run
```
$ pip install flask requests
$ python3 app.py
```

#### その他
- port は 8000
- path は /

# For Dev
ngrok が便利