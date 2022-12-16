from linebot.models import *
from app.handler.richmenu import *

from linebot.models import *


def random_carousel():
    random_carousel = TemplateSendMessage(
        alt_text="下指令給狗狗情報員",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="隨機小遊戲",
                    text="選擇障礙的人，來看看今天要做什麼吧",
                    actions=[
                        MessageAction(label="今日運勢", text="[娛樂]運勢"),
                        MessageAction(label="等等吃什麼", text="[娛樂]吃什麼"),
                    ],
                ),
            ]
        ),
    )

    return random_carousel


def handle_menu(self, reply_token, em):
    if em == "運勢":
        fortune = random.choice(["超凶", "大凶", "凶", "末吉", "吉", "中吉", "大吉"])
        self.line_bot_api.reply_message(reply_token, TextSendMessage(text=fortune))
    elif em == "吃什麼":
        eat = random.choice(["熱情小7", "風雲", "水木", "小吃部", "熊本"])
        self.line_bot_api.reply_message(reply_token, TextSendMessage(text=eat))
