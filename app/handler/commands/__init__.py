''' Chatbot command  '''
import os
from modules.affair import qa_engine
#import openai
from revChatGPT.revChatGPT import Chatbot
from linebot.models import *
from app import app
from dotenv import load_dotenv
load_dotenv()
'''
def chatGPT(text):
    if text.startswith("!") or text.startswith('！'):
        text = text[1:]
    openai.api_key = os.environ['OPENAI_TOKEN']
    ans = openai.Completion.create(
       model= "text-davinci-003",
       prompt= text,
       max_tokens= 1200,
       temperature= 0.7
    )
    app.logger.info("有人問神奇海螺：" + text)
    app.logger.info("神奇海螺回答：" + ans['choices'][0]['text'].strip())
    return ans['choices'][0]['text'].strip()
'''
config = {
  "session_token": os.environ['session_token'],
  "cf_clearance": os.environ['cf_clearance'],
  "user_agent": os.environ['user_agent'],
  #"proxy": "<HTTP/HTTPS_PROXY>"
}

chatbot = Chatbot(config, conversation_id=None)

class CmdHandler:
    def __init__(self, line_bot_api, user_instance):
        self.line_bot_api = line_bot_api
        self.user = user_instance
    
    def detect(self, msg):
        '''判斷是否為chatbot command
            Params:
                - msg
            Return:
                - isCMD(bool): 若!在第一個字元
        '''

        if msg.startswith('!') or msg.startswith('！'):
            return True
        else:
            return False

    def extract_msg(self, msg):
        if msg[0]=='!':
            return msg.split("!")[1]
        elif msg[0]=='！':
            return msg.split("！")[1]
        
    def run(self, event, msg):        
        # intro all cmd of chatbot
        if msg=='!' or msg=='！':
            self.line_bot_api.reply_message(event.reply_token, TextSendMessage(text="在你要打的句子面前加上驚嘆號 (！)，就能召喚神奇海螺囉"))
        # 執行 cmd    
        else:
            user_message = event.message.text
            print(user_message)
            response = chatbot.get_chat_response((user_message), output="text")
            print(response)
            # Get opengpt's response
            openai_response = response["message"]
            self.line_bot_api.reply_message(event.reply_token, TextSendMessage(text=openai_response))
            
'''
usage:
elif event.message.text!='你絕對不會輸入這個文字':
     line_bot_api.reply_message(  # 回復傳入的訊息文字
     event.reply_token,
     TextSendMessage(text=chatGPT(event.message.text))
     )
'''