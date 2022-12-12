from linebot.models import *

def intro_carousel():
    carousel_template = TemplateSendMessage(        
        alt_text = '下指令給狗狗情報員',
        template = CarouselTemplate(  
            columns = [
                CarouselColumn(
                    title = '分享狗狗情報員',
                    text = '快讓更多朋友認識我吧！\n @nthuchatbot',
                    actions = [
                        PostbackTemplateAction(
                            label='分享給好友',
                            data='source=richmenu&flag=commands&info=share'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '笑一下',
                    text = '聽聽四散在校園的奇聞軼事吧！讓自己輕鬆一下！',
                    actions = [
                        PostbackTemplateAction(
                            label='笑一下',
                            data='source=richmenu&flag=commands&info=newjoke'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '新增笑話',
                    text = '告訴狗狗情報員關於你在校園生活中的笑料，讓校園充滿歡笑吧！',
                    actions = [
                        PostbackTemplateAction(
                            label='新增笑話',
                            data='source=richmenu&flag=commands&info=addjoke'
                        )
                    ]
                ),
                CarouselColumn(
                    title = '問題回饋',
                    text = '我跟校園狗狗情報員溝通不良，想要回報問題或提供意見',
                    actions = [
                        PostbackTemplateAction(
                            label='問題回饋',
                            data='source=richmenu&flag=commands&info=feedback'
                        )
                    ]
                ),
            ]
        )
    )

    return carousel_template

def share_template():
    # ! -> 分享給好友
    bubble_json = '''
    {{
        "type": "bubble",
        "size": "mega",
        "header": {{
            "type": "box",
            "layout": "baseline",
            "contents": [
            {{
                "type": "icon",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png",
                "offsetStart": "10px"
            }},
            {{
                "type": "text",
                "text": "掃描加入 — 清華校園情報員",
                "offsetStart": "25px",
                "color": "#FFFFFF",
                "weight": "bold",
                "adjustMode": "shrink-to-fit"
            }}
            ],
            "backgroundColor": "#6F00D2",
            "borderWidth": "none",
            "cornerRadius": "none",
            "offsetTop": "none"
        }},
        "hero": {{
            "type": "image",
            "url": "https://i.imgur.com/40t9Qo0.png",
            "position": "relative",
            "margin": "none",
            "align": "center",
            "gravity": "center",
            "offsetTop": "lg",
            "size": "5xl"
        }},
        "body": {{
            "type": "box",
            "layout": "vertical",
            "contents": [
            {{
                "type": "text",
                "text": "@nthuchatbot",
                "color": "#7B7B7B",
                "align": "center",
                "size": "md",
                "offsetTop": "none"
            }},
            {{
                "type": "box",
                "layout": "horizontal",
                "contents": [],
                "justifyContent": "center",
                "alignItems": "center",
                "offsetEnd": "none",
                "offsetBottom": "md",
                "spacing": "none",
                "margin": "lg",
                "borderWidth": "none",
                "cornerRadius": "none",
                "paddingBottom": "none",
                "paddingTop": "none",
                "paddingAll": "none",
                "paddingStart": "none"
            }},
            {{
                "type": "button",
                "action": {{
                "type": "uri",
                "label": "分享給LINE好友",
                "uri": "https://line.me/R/nv/recommendOA/@nthuchatbot"
                }},
                "style": "secondary",
                "height": "sm",
                "offsetTop": "sm",
                "margin": "none"
            }}
            ],
            "spacing": "none",
            "margin": "none",
            "borderWidth": "none",
            "offsetBottom": "sm",
            "offsetTop": "none",
            "paddingBottom": "xxl"
        }}
    }}
    '''.format()

    return bubble_json