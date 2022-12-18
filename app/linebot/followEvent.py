"""
1. 獲取用戶的 user_id
2. 使用 user API 將用戶 user_id 插入到資料庫中
3. 向新用戶發送歡迎訊息
4. 此處也使用了 LineBotHandler 來處理 FollowEvent 事件。
"""

from linebot.models import *
from app import app
from app.linebot import line_bot_api, handler, user

# 新好友歡迎(insert user id)
@handler.add(FollowEvent)
def handle_follow(event):
    user_id = event.source.user_id
    user.insertOne(user_id)
    app.logger.info("Got Follow event:" + event.source.user_id)
    welcome_text = """(profile) 初次見面！我是清大校園情報員，你可以叫我狗狗情報員！生活上的大小事，只要是你遇到的問題，我都會努力幫你解決唷！
    
你可以~~ฅ'ω'ฅ
🚩取得/詢問新型冠狀病毒資訊！
🚩索取校巴時刻表
🚩詢問校務相關問題💬
🚩或讓本汪帶你在清大趴趴走！ 

身為一個好的情報員，有任何消息我也會盡快回報的！！

如果覺得本汪哪裡不好，想給我建議
或感到無聊想聽笑話或想分享笑話
請輸入〝！〞會有額外的功能唷

作為一隻狗狗，有時候會太熱情，如果覺得我有點吵的話，請將「提醒」功能關閉就好📵，千萬不要封鎖本汪好嗎，我一定會乖乖的喔！
    """
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=welcome_text))
