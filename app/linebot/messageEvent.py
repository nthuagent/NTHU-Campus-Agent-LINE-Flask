"""
這段程式碼是用於處理來自使用者的訊息，首先會檢查使用者輸入的文字是否為指令，如果是，則會執行相應的指令。
如果不是，則會檢查是否為選單選項，如果是，則會執行相應的選單選項。
最後，如果輸入的文字既不是指令也不是選單選項，則會檢查使用者的 flag 是否為非 init，如果是，則會執行 flag 相應的流程。
"""

from linebot.models import *

from app.linebot import line_bot_api, handler, user
from app.handler import *

cmd_handler = CmdHandler(line_bot_api, user)
richmenu_handler = RichmenuHandler(line_bot_api, user)
flag_handler = FlagHandler(line_bot_api, user)
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.user_id  # 使用者ID
    message_text = event.message.text  # 使用者訊息

    flag, err = user.getFlag(user_id)
    if err:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="訊息處理失敗 嗷嗷qq。你可以寄信到 nthuchatbot@gmail.com或聯絡粉專，讓他們知道狀況！"
            ),
        )

    print("user_id: ", user_id)
    print("flag: ", flag)
    print("message_text: ", message_text)

    # 選單事件
    if richmenu_handler.detect(message_text):
        print("is richmenu:", richmenu_handler.detect(message_text))
        user.initFlag(user_id)
        richmenu_handler.run(event, message_text)

    # 指令事件
    if cmd_handler.detect(message_text):
        user.initFlag(user_id)
        cmd_handler.run(event, message_text)

    # flag流程
    elif flag != "init":
        flag_handler.run(event, flag)
