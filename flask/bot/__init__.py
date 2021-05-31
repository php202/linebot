# git remote add origin https://github.com/php202/linebot.git
# git branch -M main
# git push -u origin main
import os
from flask import Flask, abort, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


def create_app():

    app = Flask(__name__)

    line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
    handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))

    @app.route("/callback", methods=["GET", "POST"])
    def callback():

        if request.method == "GET":
            return "Hello GCP"
        if request.method == "POST":
            signature = request.headers["X-Line-Signature"]
            body = request.get_data(as_text=True)

            try:
                handler.handle(body, signature)
            except InvalidSignatureError:
                abort(400)

            return "OK"


    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        get_message = event.message.text

        # Send To Line
        reply = TextSendMessage(text=f"{get_message}")
        line_bot_api.reply_message(event.reply_token, reply)

        
    return app
