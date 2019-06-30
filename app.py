from config import Config
from json import dumps
from requests import post
from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/', methods=['POST'])
def http_post():
    if not is_bot(request.form):
        send(request.form)
    return ''


def main():
    app.run(host='0.0.0.0', port=8000)


def is_bot(form):
    return form['user_name'] is 'slackbot'


def send(form):
    to_workspace = form['trigger_word']
    webhook_url = Config.ws_wh_dict.get(to_workspace)

    # TODO: logging here

    if webhook_url is None:
        return

    payload_dict = {
        'text': form['text'],
        'username': "{} : {}".format(
            form['team_domain'],
            form['user_name']
        )
    }

    r = post(webhook_url, data=dumps(payload_dict))


if __name__ == '__main__':
    main()
