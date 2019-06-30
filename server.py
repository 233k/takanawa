from os import getenv
from flask import Flask
from flask import request


app = Flask(__name__)


@app.route("/", methods=["POST"])
def post():
    if request.form['user_name'] != 'slackbot':
        send(request.form)
    return "hoge"


def main():
    app.run(host='0.0.0.0', port=8000)


def send(form):
    import json
    import requests
    
    SLACK_WEBHOOK = getenv('SLACK_WEBHOOK')

    payload_dic = {
        "text": form['text'],
        "username": form['user_name'],
    }

    r = requests.post(SLACK_WEBHOOK, data=json.dumps(payload_dic))

if __name__ == "__main__":
    main()

