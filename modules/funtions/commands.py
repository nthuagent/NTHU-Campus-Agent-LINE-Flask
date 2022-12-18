"""
這段程式碼是一個處理使用者輸入訊息的類別，可以處理使用者輸入的聊天機器人指令，例如：

!笑一下：顯示一則笑話
!新增笑話：新增一則笑話
!問題回饋：提供給使用者回饋問題的功能
這個類別會在收到使用者的訊息後，檢查使用者是否輸入了指令，並且執行對應的指令。例如，若使用者輸入了 !笑一下，類別會從 API 拉取一則笑話，並且回傳給使用者。
"""

""" Chatbot command  """

from linebot.models import *

from API import AndxAPI
from modules.funtions import introT


class CmdHandler:
    def __init__(self, line_bot_api, user_instance):
        self.line_bot_api = line_bot_api
        self.user = user_instance

    def detect(self, msg):
        """判斷是否為chatbot command
        Params:
            - msg
        Return:
            - isCMD(bool): 若!在第一個字元
        """

        if msg[0] == "!" or msg[0] == "！":
            return True
        else:
            return False

    def extract_msg(self, msg):
        if msg[0] == "!":
            return msg.split("!")[1]
        elif msg[0] == "！":
            return msg.split("！")[1]

    def run(self, event, msg):
        user_id = event.source.user_id
        reply_token = event.reply_token

        # intro all cmd of chatbot
        if msg == "!" or msg == "！":
            self.line_bot_api.reply_message(reply_token, introT.intro_carousel())
        # 執行 cmd
        else:
            em = self.extract_msg(msg)

            if em == "笑一下":
                andx = AndxAPI()
                anecdote, err = andx.getOne()
                if err:
                    # 沒笑話
                    self.line_bot_api.reply_message(
                        reply_token, TextSendMessage(text="沒找到笑話")
                    )
                    print(err)
                else:
                    self.line_bot_api.reply_message(
                        reply_token, TextSendMessage(text=anecdote)
                    )

            elif em == "新增笑話":
                self.line_bot_api.reply_message(
                    reply_token, TextSendMessage(text="說吧！有什麼笑話這麼好笑？")
                )
                self.user.setFlag(user_id, "andx_insert")

            elif em == "問題回饋":
                self.line_bot_api.reply_message(
                    reply_token, TextSendMessage(text="你有什麼意見或問題呢？告訴本汪，盡快為你處理！")
                )
                self.user.setFlag(user_id, "feedback")
