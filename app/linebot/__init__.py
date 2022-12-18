"""
1. 使用 os 模組取得環境變數 LINE_OFFICIAL_TOKEN 和 LINE_WEBHOOK_STRING，這些環境變數裡面存放了當前程式所使用的 LINE token 跟 webhook。
2. 建立一個 LINEBotApi 物件，並且利用第一步取得的 token 初始化。
3. 建立一個 WebhookHandler 物件，並且利用第一步取得的 webhook 初始化。
4. 建立一個 UserAPI 物件，用來提供與使用者相關的操作，例如取得使用者目前的狀態。
"""

import os
from API import TokenAPI, UserAPI
from linebot import LineBotApi, WebhookHandler

from dotenv import load_dotenv

load_dotenv()
token = os.environ["LINE_OFFICIAL_TOKEN"]
webhook = os.environ["LINE_WEBHOOK_STRING"]

# Chatbot
line_bot_api = LineBotApi(token)
handler = WebhookHandler(webhook)

# user instance
user = UserAPI()
