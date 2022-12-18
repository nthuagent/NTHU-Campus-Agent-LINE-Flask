"""
這段程式碼主要是用來監聽來自 /callback 的 POST 請求，並處理請求的資料。
在處理請求時，會驗證簽章是否有效，並使用 LineBotApi 和 WebhookHandler 來處理請求。
如果簽章無效，則會回應 400 錯誤碼。
"""

from app import app
from flask import Flask, request, abort
from linebot.exceptions import InvalidSignatureError
from app.linebot import handler


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"
