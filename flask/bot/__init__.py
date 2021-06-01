# git remote add origin https://github.com/php202/linebot.git
# git branch -M main
# git push -u origin main
# http://34.134.77.7/

# sudo su
# git pull
# docker-compose up --build
import os
from flask import Flask, abort, request, reder_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from line import linefunction

def create_app():

    app = Flask(__name__)

    line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
    handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))

    #首頁去處
    @app.route("/")
    def home():
        linefunction.push(event)
        return render_template("home.html")

    #line驗證
    @app.route("/callback", methods=["GET", "POST"])
    def callback():
        linefunction.callback()

    #相關訊息
    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        try:
            linefunction.findimg()
        except:
            print("找不到圖片")
            linefunction.echo(event)

        
    return app
