from datetime import datetime
from linebot.models import *

import json
from app import app
from API import UserAPI, BusAPI, DataAPI
from app.handler.richmenu.template import epidemicT, recnewsT, broadcastT
from utils import recnewUtil
from modules.map import locationT, mapUtil
from modules.bus import busT
from modules.recruitment import recruitmentT, recruitmentUtil
from modules.affair import affairT, phoneT, stopT
from modules.funtions import introT

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

        if msg[0:4] == '[選單]':
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
            self.line_bot_api.reply_message(reply_token, affairT.affair_info_carousel())
            
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
        # elif em == "新增新型冠狀病毒相關問題":  #ˋ4/5先拔除
        #     self.line_bot_api.reply_message(reply_token, epidemicT.epidemic_feedback())
        #     self.user.setFlag(user_id, 'epidemic_feedback')
        elif em == "防疫Q&A":
            self.line_bot_api.reply_message(reply_token, epidemicT.qa_info())
            self.user.setFlag(user_id, 'epidemic_qa')
            
        elif em == "神奇海螺":
            self.line_bot_api.reply_message(reply_token, introT.intro_carousel())
        
        # elif em == "新型冠狀病毒相關公告":
        #     self.line_bot_api.reply_message(reply_token, epidemicT.epidemic_info_carousel())

        # 確認機制寫在選單裡面，確保使用者不會卡死在主動推播選單。

        #elif em == "哈哈":
            # TODO: Fix richmenu
            # self.line_bot_api.link_rich_menu_to_user(user_id, "richmenu-40a91b3a104119f90757b48253ab9c11")
        #elif em == "運勢":
        #    self.line_bot_api.reply_message(reply_token, introT.intro_carousel())
        # TODO: USR專區
        # elif em == '清華大學USR':
        #     self.line_bot_api.reply_message(reply_token, usrT.usr_carousel())



class PostbackHandler:
    def __init__(self, line_bot_api, user_instance):
        self.line_bot_api = line_bot_api
        self.user = user_instance

    def run(self, event, param):
        user_id = event.source.user_id
        reply_token = event.reply_token

        user = UserAPI()
        _data = DataAPI()

        if param.get('flag') == 'epidemic':
            if param.get('info') == 'qa':  
                self.line_bot_api.reply_message(reply_token, epidemicT.qa_info())
                self.user.setFlag(user_id, 'epidemic_qa')
            if param.get('info') == 'students':
                epid_content, err = _data.getEpid('students')
                if err:
                    self.line_bot_api.reply_message(reply_token, TextSendMessage(text='取得防疫資訊失敗 嗷嗷qq。你可以透過意見回饋讓情報團隊了解情況！'))
                else:
                    self.line_bot_api.reply_message(reply_token, epidemicT.students_carousel_render(epid_content))
                    # self.line_bot_api.reply_message(reply_token, epidemicT.students_info())

            # 屬於純text的防疫category
            else:
                epid_category = param.get('info')
                epid_content, err = _data.getEpid(epid_category)
                if err:
                    self.line_bot_api.reply_message(reply_token, TextSendMessage(text='取得防疫資訊失敗 嗷嗷qq。你可以透過意見回饋讓情報團隊了解情況！'))
                else:
                    self.line_bot_api.reply_message(reply_token, epidemicT.epid_content_render(epid_content))

            # elif param.get('info') == 'boarders':
            #     self.line_bot_api.reply_message(reply_token, epidemicT.boarders_info())
            # elif param.get('info') == 'backtw':
            #     self.line_bot_api.reply_message(reply_token, epidemicT.backtw_info())
            # elif param.get('info') == 'isolation':
            #     self.line_bot_api.reply_message(reply_token, epidemicT.isolation_info())
            # elif param.get('info') == 'foreign':
            #     self.line_bot_api.reply_message(reply_token, epidemicT.foreign_info())
            # elif param.get('info') == 'chinastudent':
            #     self.line_bot_api.reply_message(reply_token, epidemicT.chinastudent_info())
            # elif param.get('info') == 'tkm':
            #     self.line_bot_api.reply_message(reply_token, epidemicT.tkm_info())
            # elif param.get('info') == 'change2tkm':
            #     self.line_bot_api.reply_message(reply_token, epidemicT.change2tkm_info())
            # elif param.get('info') == 'contact':
            #     self.line_bot_api.reply_message(reply_token, epidemicT.contact_info())

        elif param.get('flag') == 'affair':
            if param.get('info') == 'qa':
                self.line_bot_api.reply_message(reply_token, affairT.qa_info())
                self.user.setFlag(user_id, 'affair_qa')
            elif param.get('info') == 'recnews':
                    self.line_bot_api.reply_message(reply_token, affairT.recNew_type())
            elif param.get('info') == 'speech':
                recnews, err = _data.getrecNews('speech')
                if err:
                    self.line_bot_api.reply_message(reply_token, TextSendMessage(text='取得活動資訊失敗 嗷嗷qq。你可以透過意見回饋讓情報團隊了解情況！'))
                elif recnews == []:
                    self.line_bot_api.reply_message(reply_token, TextSendMessage(text='目前沒有任何演講！'))
                else:
                    news = recnewUtil.create_news_list(recnews)
                    self.line_bot_api.reply_message(reply_token, recnewsT.recnew_carousel(news))
            elif param.get('info') == 'exhibition':
                recnews, err = _data.getrecNews('exhibition')
                if err:
                    self.line_bot_api.reply_message(reply_token, TextSendMessage(text='取得活動資訊失敗 嗷嗷qq。你可以透過意見回饋讓情報團隊了解情況！'))
                elif recnews == []:
                    self.line_bot_api.reply_message(reply_token, TextSendMessage(text='目前沒有任何展覽！'))
                else:
                    news = recnewUtil.create_news_list(recnews)
                    self.line_bot_api.reply_message(reply_token, recnewsT.recnew_carousel(news))
            elif param.get('info') == 'activity':
                recnews, err = _data.getrecNews('activity')
                if err:
                    self.line_bot_api.reply_message(reply_token, TextSendMessage(text='取得活動資訊失敗 嗷嗷qq。你可以透過意見回饋讓情報團隊了解情況！'))
                elif recnews == []:
                    self.line_bot_api.reply_message(reply_token, TextSendMessage(text='目前沒有任何活動！'))
                else:
                    news = recnewUtil.create_news_list(recnews)
                    self.line_bot_api.reply_message(reply_token, recnewsT.recnew_carousel(news))
            elif param.get('info') == 'phone':
                self.line_bot_api.reply_message(reply_token, phoneT.qa_info())
                self.user.setFlag(user_id, 'phone_qa')
        elif param.get('flag') == 'intro':
            if param.get('info') == 'share':
                self.line_bot_api.reply_message(reply_token, FlexSendMessage(alt_text="分享QRcode", contents=json.loads(introT.share_template())))
        elif param.get('flag') == 'bus':
            if param.get('info') == 'main_campus':
                self.line_bot_api.reply_message(reply_token, busT.main_campus_bus_img())
            elif param.get('info') == 'minor_campus':
                self.line_bot_api.reply_message(reply_token, busT.minor_campus_bus_img())
            elif param.get('info') == '83_bus':
                self.line_bot_api.reply_message(reply_token, busT.et_bus_img())


