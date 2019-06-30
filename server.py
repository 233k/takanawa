from config import Config
from json import dumps
from requests import post
from flask import Flask
from flask import request


app = Flask(__name__)


@app.route("/", methods=["POST"])
def http_post():
    if request.form['user_name'] != 'slackbot':
        send(request.form)
    return "hoge"


def main():
    app.run(host='0.0.0.0', port=8000)


def send(form):
    to_workspace = form['trigger_word']
    webhook_url = Config.ws_wh_dict[to_workspace]

    payload_dict = {
        "text": form['text'],
        "username": form['user_name'],
    }

    # TODO: logging here
    r = post(webhook_url, data=dumps(payload_dict))


if __name__ == "__main__":
    main()

