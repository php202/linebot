# -*- coding: utf-8 -*-
# git remote add origin https://github.com/php202/linebot.git
# git branch -M main
# git push -u origin main
# ssh root@34.134.77.7

# sudo su
# git pull
# docker-compose up --build
from __future__ import unicode_literals
import os
from flask import Flask, abort, request, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from line import linefunction

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('聊天機器人的 Chennel access token')
handler = WebhookHandler('聊天機器人的 Channel secret')


#首頁去處
@app.route("/")
def home():
    # linefunction.push(event)
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

if __name__ == "__main__":
    app.run()        

