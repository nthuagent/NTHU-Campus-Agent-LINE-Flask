from datetime import datetime
from linebot.models import *

import json
from app import app
from API import AndxAPI, UserAPI, BusAPI, DataAPI

from modules.affair import affairT, recnewsT, recnewUtil, stopT, phoneT, epidemicT
from modules.funtions import introT
from modules.joke import jokeT
from modules.data import dataT


class PostbackHandler:
    def __init__(self, line_bot_api, user_instance):
        self.line_bot_api = line_bot_api
        self.user = user_instance

    def run(self, event, param):
        user_id = event.source.user_id
        reply_token = event.reply_token

        flag = param.flag
        source = param.source
        info = param.info

        if flag == "epidemic":
            if info == "qa":
                self.line_bot_api.reply_message(reply_token, epidemicT.qa_info())
                self.user.setFlag(user_id, "epidemic_qa")
            else:
                epid_content = dataT.get_epid(info)
                if not epid_content:
                    self.line_bot_api.reply_message(
                        reply_token,
                        TextSendMessage(text="取得防疫資訊失敗 嗷嗷qq。你可以透過意見回饋讓情報團隊了解情況！"),
                    )
                else:
                    self.line_bot_api.reply_message(
                        reply_token, epidemicT.epid_content_render(epid_content)
                    )

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

        elif flag == "affair":
            if info == "qa":
                self.line_bot_api.reply_message(reply_token, affairT.qa_info())
                self.user.setFlag(user_id, "affair_qa")
            elif info == "recnews":
                self.line_bot_api.reply_message(reply_token, affairT.recNew_type())
            elif info == "speech":
                recnews = dataT.get_rec_news("speech")
                if recnews == None:
                    self.line_bot_api.reply_message(
                        reply_token,
                        TextSendMessage(text="取得活動資訊失敗 嗷嗷qq。你可以透過意見回饋讓情報團隊了解情況！"),
                    )
                elif recnews == []:
                    self.line_bot_api.reply_message(
                        reply_token, TextSendMessage(text="目前沒有任何演講！")
                    )
                else:
                    news = recnewUtil.create_news_list(recnews)
                    self.line_bot_api.reply_message(
                        reply_token, recnewsT.recnew_carousel(news)
                    )
            elif info == "exhibition":
                recnews = dataT.get_rec_news("exhibition")
                if recnews == None:
                    self.line_bot_api.reply_message(
                        reply_token,
                        TextSendMessage(text="取得活動資訊失敗 嗷嗷qq。你可以透過意見回饋讓情報團隊了解情況！"),
                    )
                elif recnews == []:
                    self.line_bot_api.reply_message(
                        reply_token, TextSendMessage(text="目前沒有任何展覽！")
                    )
                else:
                    news = recnewUtil.create_news_list(recnews)
                    self.line_bot_api.reply_message(
                        reply_token, recnewsT.recnew_carousel(news)
                    )
            elif info == "activity":
                recnews = dataT.getrecNews("activity")
                if err == None:
                    self.line_bot_api.reply_message(
                        reply_token,
                        TextSendMessage(text="取得活動資訊失敗 嗷嗷qq。你可以透過意見回饋讓情報團隊了解情況！"),
                    )
                elif recnews == []:
                    self.line_bot_api.reply_message(
                        reply_token, TextSendMessage(text="目前沒有任何活動！")
                    )
                else:
                    news = recnewUtil.create_news_list(recnews)
                    self.line_bot_api.reply_message(
                        reply_token, recnewsT.recnew_carousel(news)
                    )
            elif info == "phone":
                self.line_bot_api.reply_message(reply_token, phoneT.qa_info())
                self.user.setFlag(user_id, "phone_qa")
        elif flag == "commands":
            if info == "share":
                self.line_bot_api.reply_message(
                    reply_token,
                    FlexSendMessage(
                        alt_text="分享QRcode",
                        contents=json.loads(introT.share_template()),
                    ),
                )
            elif info == "newjoke":
                anecdote = get_joke()
                if not anecdote:
                    # 沒笑話
                    self.line_bot_api.reply_message(
                        reply_token, TextSendMessage(text="沒找到笑話")
                    )
                    print(err)
                else:
                    self.line_bot_api.reply_message(
                        reply_token, TextSendMessage(text=anecdote)
                    )
            elif info == "addjoke":
                self.line_bot_api.reply_message(
                    reply_token, TextSendMessage(text="說吧！有什麼笑話這麼好笑？")
                )
                self.user.setFlag(user_id, "andx_insert")
            elif info == "feedback":
                self.line_bot_api.reply_message(
                    reply_token, TextSendMessage(text="你有什麼意見或問題呢？告訴本汪，盡快為你處理！")
                )
                self.user.setFlag(user_id, "feedback")
