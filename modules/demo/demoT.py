from linebot.models import *
from app.handler.richmenu import *

def handle_menu(self, reply_token, em):
    if em == "DEMO1":
        self.line_bot_api.reply_message(reply_token, tzaiwu_space())
    elif em == "DEMO2":
        self.line_bot_api.reply_message(reply_token, bus_route_template())
    elif em == "DEMO3":
        self.line_bot_api.reply_message(reply_token, ok_button())
    elif em == "DEMO4":
        self.line_bot_api.reply_message(reply_token, image_temp())

#def demoT_intro():
#    reply_arr=[]
#    reply_arr.append(tzaiwu_space())
#    return reply_arr

def demoT_intro(): #公車路線清單
    demoT_intro = TemplateSendMessage(
        alt_text='DEMO',
        template=ButtonsTemplate(
            title='DEMO',
            text='請選擇你要使用的 DEMO',
            actions=[
                MessageAction(
                    label='tzaiwu_space',
                    text='[示範]DEMO1'
                ),
                MessageAction(
                    label='bus_route_template',
                    text='[示範]DEMO2'
                ),
                MessageAction(
                    label='ok_button',
                    text='[示範]DEMO3'
                ),
                MessageAction(
                    label='image_temp',
                    text='[示範]DEMO4'
                )
                # # TODO: 動態校車
                # PostbackTemplateAction(
                #     label='校本部校車動態查詢',
                #     data='source=richmenu&flag=bus&info=dyn_search'
                # )
            ]
        )
    )
    return demoT_intro

def tzaiwu_space():
    tzaiwu_space = TemplateSendMessage(        
        alt_text = '載物書院專屬功能',
        template = CarouselTemplate(  
            columns = [
                CarouselColumn(
                    title = '仁齋公共空間預約表單',
                    altText = '我要借空間！',
                    text = '超過預約總時長四分之一或十分鐘內未使用，則自動取消預約，開放其他齋民直接使用空間。',
                    actions = [
                        URIAction(
                            label='仁齋空間登記！',
                            uri='https://space-64c57.web.app/'
                        ),
                        URIAction(
                            label='仁齋空間借用狀況',
                            uri='https://calendar.google.com/calendar/embed?src=oa27fmn21hoqd0hvdpg1bqlv1k%40group.calendar.google.com&ctz=Asia%2FTaipei'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '我要更大的空間！',
                    altText = '我要更大的空間！',
                    text = '如果要借用廚具請找空間管理員，在借用廚具後會獲得仁廚的優先使用權',
                    actions = [
                        URIAction(
                            label='仁齋空間登記！',
                            uri='https://forms.gle/td3pvqHQopKZmESE6'
                        ),
                        URIAction(
                            label='仁廚借用狀況',
                            uri='https://reurl.cc/WEYV4e'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '仁廚冰箱物品放置登記',
                    altText = '我想用冰箱！',
                    text = '將物品放置在仁齋二樓廚房的冰箱時，視為同意《仁齋冰箱使用條例》。',
                    actions = [
                        URIAction(
                            label='冰箱物品登記！',
                            uri='https://bit.ly/%E4%B9%BE%E6%B7%A8%E7%9A%84%E5%86%B0%E7%AE%B1'
                        ),
                        URIAction(
                            label='冰箱物品查看',
                            uri='http://bit.ly/%E7%9C%8B%E7%9C%8B%E6%9C%89%E4%BB%80%E9%BA%BC'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '仁齋圖書借用登記',
                    altText = '我想要讀書！',
                    text = '提供需要借用書籍一天以上的齋民登記，以便其他齋民得知書籍流向、以及齋團隊管理。',
                    actions = [
                        URIAction(
                            label='仁齋圖書借用',
                            uri='https://forms.gle/HZ6bjv159QNwCYic6'
                        ),
                        URIAction(
                            label='書籍借用紀錄',
                            uri='https://docs.google.com/spreadsheets/d/1MtcmbiUGx9IZxlr37uwitumMtXcwPamzdTczLQKfMA/edit?usp=sharing'
                        )
                    ]
                ),
                CarouselColumn(
                    title = 'T-house 借用登記',
                    altText = '我要借齋丘！',
                    text = '請先詳閱借用辦法及借用情況後，在填寫表單喔，感謝！如對借用辦法有任何疑問，歡迎私訊齋丘粉專！',
                    actions = [
                        URIAction(
                            label='T-house 借用表單',
                            uri='https://space-64c57.web.app/'
                        ),
                        URIAction(
                            label='T-house 借用狀況',
                            uri='https://lihi1.cc/MdAfJ'
                        )
                    ]
                ),
            ]
        )
    )
    return tzaiwu_space

def bus_route_template(): #公車路線清單
    template_list = []
    bus_route_template = TemplateSendMessage(
        alt_text='公車路線清單',
        template=ButtonsTemplate(
            title='公車路線',
            text='請選擇你要查詢的公車路線',
            actions=[
                URIAction(
                    label='公車資訊公告',
                    uri='https://affairs.site.nthu.edu.tw/p/403-1165-1065-1.php?Lang=zh-tw'
                ),
                MessageAction(
                    label='校本部公車',
                    text='[公車]校本部公車'
                ),
                MessageAction(
                    label='南大專車',
                    text='[公車]南大專車'
                ),
                MessageAction(
                    label='83路線公車',
                    text='[公車]83公車'
                )
                # # TODO: 動態校車
                # PostbackTemplateAction(
                #     label='校本部校車動態查詢',
                #     data='source=richmenu&flag=bus&info=dyn_search'
                # )
            ]
        )
    )
    template_list.append(bus_route_template)
    return template_list

def ok_button():
    confirm_template_message = TemplateSendMessage(
        alt_text='確認模板',
        template=ConfirmTemplate(
            text='你確定嗎？',
            actions=[
                PostbackAction(
                    label='postback',
                    display_text='postback text',
                    data='action=buy&itemid=1'
                ),
                MessageAction(
                    label='訊息',
                    text='訊息'
                )
            ]
        )
    )
    return confirm_template_message

def image_temp():
    image_temp = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://example.com/item1.jpg',
                    action=PostbackAction(
                        label='postback1',
                        display_text='postback text1',
                        data='action=buy&itemid=1'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://example.com/item2.jpg',
                    action=PostbackAction(
                        label='postback2',
                        display_text='postback text2',
                        data='action=buy&itemid=2'
                    )
                )
            ]
        )
    )
    return image_temp

def qa_info():
    '''校園電話Q&A'''
    QuickReply_text_message = TextSendMessage(
        text = '請輸入想要查詢的單位名稱',
        quick_reply = QuickReply(
            items = [
                QuickReplyButton(
                    image_url='https://i.imgur.com/szzgMji.png',
                    action = MessageAction(label = "校安中心", text = "校安中心"),
                ),
                QuickReplyButton(
                    image_url='https://i.imgur.com/lwoIwZa.png',
                    action = MessageAction(label = "駐衛警察隊", text = "駐衛警察隊"),
                ),
                # QuickReplyButton(
                #     image_url='https://i.imgur.com/7wGbjZJ.png',
                #     action = MessageAction(label = "清華總機", text = "清華總機"),
                # )
            ]
        )
    )
    return QuickReply_text_message