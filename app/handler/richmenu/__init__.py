from datetime import datetime
from linebot.models import *

import json
from app import app
from API import UserAPI, BusAPI, DataAPI
from app.handler.richmenu.template import epidemicT, broadcastT

from modules.affair import affairT, recnewsT, recnewUtil, stopT, phoneT
from modules.bus import busT
from modules.funtions import introT
from modules.map import locationT, mapUtil
from modules.recruitment import recruitmentT, recruitmentUtil

class RichmenuHandler:
    def __init__(self, line_bot_api, user_instance):
        self.line_bot_api = line_bot_api
        self.user = user_instance
    
    def detect(self, msg):
        '''判斷是否為選單事件
            Params:
                - msg
            Return:
                - isRichmenu(bool): 若開頭為 [選單]
        '''

        if msg.startswith('[選單]'):
            return True
        else:
            return False

    def extract_msg(self, msg):
        return msg[4:]

    def run(self, event, msg):
        em = self.extract_msg(msg)
        user_id = event.source.user_id
        reply_token = event.reply_token

        user = UserAPI()

        location = []
        items = []
        recnews = []
        news = []

        if em == "校園公車時間表": #回覆公車路線template
            self.line_bot_api.reply_message(reply_token, busT.bus_route_template())

        elif em == '清華校內工讀':
            recruitment_list = recruitmentUtil.get_list()
            self.line_bot_api.reply_message(reply_token, recruitmentT.recruitment_carousel(recruitment_list))
            
        # 確認機制寫在選單裡面，確保使用者不會卡死在主動推播選單。
        elif em == "切換主動推播":
            ids, err = user.getBroadcastAudienceIds(user_id)
            self.line_bot_api.reply_message(reply_token, broadcastT.broadcast_info(len(ids) > 0)) 
        elif em == "關閉主動推播":
            user.updateBroadcastTag(user_id, 2000000000)
            self.line_bot_api.reply_message(reply_token, TextSendMessage(text="主動推播已經關閉囉，我會安靜的汪"))
        elif em == "開啟主動推播":
            user.updateBroadcastTag(user_id, 0)
            self.line_bot_api.reply_message(reply_token, TextSendMessage(text="主動推播已經開啟囉"))
         
        elif em == "校務專區":
            reply_arr=[]
            reply_arr.append(affairT.affair_info_carousel())
            reply_arr.append(introT.intro_carousel())
            self.line_bot_api.reply_message(reply_token, reply_arr) #神奇海螺先放來這裡
            
        elif em == "校園地圖查詢":
            location, err = user.getMapRecord(user_id)
            if err:
                self.line_bot_api.reply_message(reply_token, TextSendMessage(text=err))
            elif not location:  #若取得map record為空
                self.line_bot_api.reply_message(reply_token, locationT.intro())
            elif location:
                items = locationT.create_location_list(location)
                self.line_bot_api.reply_message(reply_token, locationT.personal_intro(items))
            self.user.setFlag(user_id, 'mapping')
        
        # elif em == "新型冠狀病毒相關公告":
        #     self.line_bot_api.reply_message(reply_token, epidemicT.epidemic_info_carousel())
        # elif em == "新增新型冠狀病毒相關問題":  #ˋ4/5先拔除
        #     self.line_bot_api.reply_message(reply_token, epidemicT.epidemic_feedback())
        #     self.user.setFlag(user_id, 'epidemic_feedback')

        elif em == "防疫Q&A":
            self.line_bot_api.reply_message(reply_token, epidemicT.qa_info())
            self.user.setFlag(user_id, 'epidemic_qa')

        #elif em == "哈哈":
            # TODO: Fix richmenu
            # self.line_bot_api.link_rich_menu_to_user(user_id, "richmenu-40a91b3a104119f90757b48253ab9c11")
        #elif em == "運勢":
        #    self.line_bot_api.reply_message(reply_token, introT.intro_carousel())
        # TODO: USR專區
        # elif em == '清華大學USR':
        #     self.line_bot_api.reply_message(reply_token, usrT.usr_carousel())

