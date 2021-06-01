from flask import Flask, abort, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


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

def echo(event):
    #忽略 官方line@ 訊息
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

def findimg(event):
    q_string = {'tbm': 'isch', 'q': event.message.text}
    url = f"https://www.google.com/search?{urllib.parse.urlencode(q_string)}/"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    req = urllib.request.Request(url, headers = headers)
    conn = urllib.request.urlopen(req)
    # print('fetch conn finish')
    pattern = 'img data-src="\S*"'
    img_list = []

    for match in re.finditer(pattern, str(conn.read())):
        img_list.append(match.group()[14:-1])

    random_img_url = img_list[random.randint(0, len(img_list)+1)]
    # print('fetch img url finish')
    print(random_img_url)
    line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url=random_img_url,preview_image_url=random_img_url))

def push(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))