"""
這段程式碼用來處理 Line Bot 上接收到的 postback 事件。
當使用者在 Line Bot 的選單中選擇某個項目時，Line Bot 會發送 postback 事件來讓程式處理。
程式會將 postback 事件中的資料（data）解析並傳入 postback_handler.run 函數中進行處理。
"""

from linebot.models import *

from app.linebot import line_bot_api, handler, user
from app.handler.postback import PostbackHandler, postbackUtil

postback_handler = PostbackHandler(line_bot_api, user)

# 監聽 Postback
# Richmenu: epidemic
@handler.add(PostbackEvent)
def handle_postback(event):
    data = event.postback.data
    param = postbackUtil.parse(data)

    postback_handler.run(event, param)
