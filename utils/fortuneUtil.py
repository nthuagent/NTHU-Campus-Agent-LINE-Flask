from linebot.models import *
from random import choice

def tools_template(): #公車路線清單
    template_list = []
    bus_route_template = TemplateSendMessage(
        alt_text='工具箱',
        template=ButtonsTemplate(
            title='工具箱',
            text='請選擇你要使用的工具',
            actions=[
                URITemplateAction(
                    label='公車資訊公告',
                    uri='https://affairs.site.nthu.edu.tw/p/403-1165-1065-1.php?Lang=zh-tw'
                ),
                PostbackTemplateAction(
                    label='校本部公車',
                    data='source=richmenu&flag=bus&info=main_campus'
                ),
                PostbackTemplateAction(
                    label='南大專車',
                    data='source=richmenu&flag=bus&info=minor_campus'
                ),
                PostbackTemplateAction(
                    label='83路線公車',
                    data='source=richmenu&flag=bus&info=83_bus'
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
'''
def create_quick_replies():
    # 隨機出現運勢按鈕
    fortune = QuickReplyButton(
        action = MessageAction(label = '運勢', text = '運勢'),
    )

    # 隨機出現天氣按鈕
    weather = QuickReplyButton(
        action = MessageAction(label = '天氣', text = '天氣'),
    )

    # 建立快速選單按鈕列表
    quick_replies_list = [fortune, weather]

    # 回傳快速選單按鈕列表
    return quick_replies_list

# 如果用戶輸入運勢，則隨機出現運勢
def handle_message(message):
  if '運勢' in message:
    fortune = ['大吉', '吉', '小吉', '小凶', '凶', '大凶']
    return random.choice(fortune)
'''