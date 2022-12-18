from datetime import datetime
from linebot.models import *

import random
from app import app
from API import UserAPI

from modules.affair import affairT, epidemicT
from modules.bus import busT
from modules.broadcast import broadcastT
from modules.funtions import introT
from modules.map import locationT
from modules.recruitment import recruitmentT, recruitmentUtil
from modules.tzaiwu import tzaiwuT
from modules.games import randomT
from modules.demo import demoT


class RichmenuHandler:
    def __init__(self, line_bot_api, user_instance):
        self.line_bot_api = line_bot_api
        self.user = user_instance

    def detect(self, msg):
        # 判斷是否為選單事件
        #   Params:
        #       - msg
        #   Return:
        #       - isRichmenu(bool): 若開頭為 [選單]
        if msg.startswith("["):
            return True
        else:
            return False

    def run(self, event, msg):
        # LINE API Document:
        # https://developers.line.biz/en/docs/messaging-api/overview/
        # Python SDK Document:
        # https://github.com/line/line-bot-sdk-python
        user_id = event.source.user_id
        reply_token = event.reply_token

        # 拆分 msg 字串，注意選單需要是兩個字
        # example: [選單]你好
        # origin = [選單]你好
        # menu = [選單]
        # em = [你好]
        origin = msg  # original message
        menu = msg[0:4]  # input menu
        em = msg[4:]  # extract message
        print("trigger: ", menu)

        user = UserAPI()

        if menu == "[選單]":
            if em == "校園公車時間表":
                self.line_bot_api.reply_message(reply_token, busT.bus_route_template())

            elif em == "清華校內工讀":
                recruitment_list = recruitmentUtil.get_list()
                self.line_bot_api.reply_message(
                    reply_token, recruitmentT.recruitment_carousel(recruitment_list)
                )

            # 確認機制寫在選單裡面，確保使用者不會卡死在主動推播選單。
            elif em == "切換主動推播":
                ids, err = user.getBroadcastAudienceIds(user_id)
                self.line_bot_api.reply_message(
                    reply_token, broadcastT.broadcast_info(len(ids) > 0)
                )
            elif em == "關閉主動推播":
                user.updateBroadcastTag(user_id, 2000000000)
                self.line_bot_api.reply_message(
                    reply_token, TextSendMessage(text="主動推播已經關閉囉，我會安靜的汪")
                )
            elif em == "開啟主動推播":
                user.updateBroadcastTag(user_id, 0)
                self.line_bot_api.reply_message(
                    reply_token, TextSendMessage(text="主動推播已經開啟囉")
                )

            elif em == "校務專區":
                reply_arr = []
                reply_arr.append(affairT.affair_info_carousel())
                reply_arr.append(introT.intro_carousel())
                reply_arr.append(randomT.random_carousel())
                self.line_bot_api.reply_message(reply_token, reply_arr)  # 神奇海螺先放來這裡

            elif em == "校園地圖查詢":
                location, err = user.getMapRecord(user_id)
                if err:
                    self.line_bot_api.reply_message(
                        reply_token, TextSendMessage(text=err)
                    )
                elif not location:  # 若取得map record為空
                    self.line_bot_api.reply_message(reply_token, locationT.intro())
                elif location:
                    items = locationT.create_location_list(location)
                    self.line_bot_api.reply_message(
                        reply_token, locationT.personal_intro(items)
                    )
                self.user.setFlag(user_id, "mapping")

            elif em == "防疫Q&A":
                self.line_bot_api.reply_message(reply_token, epidemicT.qa_info())
                self.user.setFlag(user_id, "epidemic_qa")

            elif em == "載物書院":
                self.line_bot_api.reply_message(reply_token, tzaiwuT.tzaiwu_intro())

            elif em == "DEMO" or "demo":  # 演示各 Template
                self.line_bot_api.reply_message(reply_token, demoT.demoT_intro())

        elif menu == "[公車]":
            self.line_bot_api.reply_message(reply_token, busT.handle_menu(em))

        elif menu == "[載物]":
            self.line_bot_api.reply_message(reply_token, tzaiwuT.handle_menu(em))

        elif menu == "[娛樂]":
            self.line_bot_api.reply_message(reply_token, demoT.handle_menu(em))

        elif menu == "[示範]":
            self.line_bot_api.reply_message(reply_token, demoT.handle_menu(em))

        # elif em == "新型冠狀病毒相關公告":
        #     self.line_bot_api.reply_message(reply_token, epidemicT.epidemic_info_carousel())
        # elif em == "新增新型冠狀病毒相關問題":  #ˋ4/5先拔除
        #     self.line_bot_api.reply_message(reply_token, epidemicT.epidemic_feedback())
        #     self.user.setFlag(user_id, 'epidemic_feedback')
        # elif em == "哈哈":
        # TODO: Fix richmenu
        # self.line_bot_api.link_rich_menu_to_user(user_id, "richmenu-40a91b3a104119f90757b48253ab9c11")
        # TODO: USR專區
        # elif em == '清華大學USR':
        #     self.line_bot_api.reply_message(reply_token, usrT.usr_carousel())
