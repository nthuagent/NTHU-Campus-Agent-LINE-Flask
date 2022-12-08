'''
這段程式碼用來在 Line Bot 中用來產生快速回覆按鈕。
函數接受一個地點名稱的列表作為輸入，並隨機挑選一些地點名稱補齊至 10 個，然後將這些地點名稱轉換成快速回覆按鈕並返回。
這些按鈕可以在 Line Bot 中使用，讓使用者選擇輸入地點名稱。
'''

from linebot.models import *
from random import choice

def create_location_list(location):
    item = []
    location_list = []
    for i in location:
        item.append(i)
    if len(item) != 10: #補齊至10個地點
        random_location = ['第一綜合大樓','第二綜合大樓','第三綜合大樓','學務處','總務處','註冊組','人文社會學院','水木生活中心','學生住宿組'
                            ,'小吃部','體育館','校友體育館','機車塔','清交小徑','奕園停車場','北校門口','南校門口','圖書館','風雲樓','駐警隊']
        while len(item) != 10:
            re = ''
            l = choice(random_location)
            for i in item:
                if l == i:
                    re = 'repeat'          
            if re != 'repeat':
                item.append(l)
    for loc in item:
        location_button = QuickReplyButton(
            action = MessageAction(label = loc, text = loc),
        )
        location_list.append(location_button)

    return location_list