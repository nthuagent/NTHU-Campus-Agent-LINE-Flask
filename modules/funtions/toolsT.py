from linebot.models import *

def tools_carousel():
    tools_template = TemplateSendMessage(        
        alt_text = '下指令給狗狗情報員',
        template = CarouselTemplate(  
            columns = [
                 CarouselColumn(
                    title = '隨機小遊戲',
                    text = '選擇障礙的人，來看看今天要做什麼吧',
                    actions = [
                        MessageAction(
                            label='今日運勢',
                            text='[隨機]運勢'
                        ),
                        MessageAction(
                            label='等等吃什麼',
                            text='[隨機]吃什麼'
                        )
                    ]
                ),
            ]
        )
    )

    return tools_template