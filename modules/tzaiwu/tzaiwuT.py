from linebot.models import *
from app.handler.richmenu import *


def handle_menu(em):
    if em == "借用設備與空間":
        return tzaiwu_space()
    elif em == "修繕設備與空間":
        return tzaiwu_fix()


def tzaiwu_intro():
    tzaiwu_intro = TemplateSendMessage(
        alt_text="載物書院專屬功能",
        template=CarouselTemplate(
            imageAspectRatio="rectangle",
            imageSize="cover",
            columns=[
                CarouselColumn(
                    # thumbnailImageUrl = 'https://.JPG',
                    # imageBackgroundColor = '#111111',
                    title="載物填表單",
                    text="載物書院有好多表單要填，情報員幫你集合在這裡！",
                    actions=[
                        MessageAction(label="我想要借設備或空間！", text="[載物]借用設備與空間"),
                        MessageAction(label="他們壞了，我想要修理他們！", text="[載物]修繕設備與空間"),
                        # 務必記得，每個 CarouselColumn 的 Action 數量務必相同！
                        # 我被搞到心態沒了
                        URIAction(
                            label="看看目前的空間借用狀況",
                            uri="https://calendar.google.com/calendar/embed?src=oa27fmn21hoqd0hvdpg1bqlv1k%40group.calendar.google.com&ctz=Asia%2FTaipei",
                        ),
                    ],
                )
                # CarouselColumn( #開發中，暫時停用
                #    thumbnailImageUrl = 'https://.JPG',
                #    imageBackgroundColor = '#111111',
                #    title = '載物看小組',
                #    text = '載物書院那麼多小組讓你眼花撩亂嗎？情報員都整理好囉！',
                #    actions = [
                #        MessageAction(
                #            label='有什麼載物小組？',
                #            text='[載物]載物小組'
                #        ),
                #        MessageAction(
                #            label='有什麼產創小組？',
                #            text='[載物]產創小組'
                #        ),
                #        MessageAction(
                #            label='有什麼服學小組？',
                #            text='[載物]服學小組'
                #        )
                #    ]
                # )
            ],
        ),
    )
    return tzaiwu_intro


def tzaiwu_space():
    tzaiwu_space = TemplateSendMessage(
        alt_text="載物書院專屬功能",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="仁齋公共空間預約表單",
                    altText="我要借空間！",
                    text="超過預約總時長四分之一或十分鐘內未使用，則自動取消預約，開放其他齋民直接使用空間。",
                    actions=[
                        URIAction(label="仁齋空間登記！", uri="https://space-64c57.web.app/"),
                        URIAction(
                            label="仁齋空間借用狀況",
                            uri="https://calendar.google.com/calendar/embed?src=oa27fmn21hoqd0hvdpg1bqlv1k%40group.calendar.google.com&ctz=Asia%2FTaipei",
                        ),
                    ],
                ),
                CarouselColumn(
                    title="我想要借用仁廚！",
                    altText="我要更大的空間！",
                    text="如果要（合法的）借用廚具請找空間管理員，在借用廚具後會獲得仁廚的優先使用權",
                    actions=[
                        URIAction(
                            label="仁廚空間登記！", uri="https://forms.gle/td3pvqHQopKZmESE6"
                        ),
                        URIAction(label="仁廚借用狀況", uri="https://reurl.cc/WEYV4e"),
                    ],
                ),
                CarouselColumn(
                    title="仁廚冰箱物品放置登記",
                    altText="我想用冰箱！",
                    text="將物品放置在仁齋二樓廚房的冰箱時，視為同意《仁齋冰箱使用條例》。",
                    actions=[
                        URIAction(
                            label="冰箱物品登記！",
                            uri="https://bit.ly/%E4%B9%BE%E6%B7%A8%E7%9A%84%E5%86%B0%E7%AE%B1",
                        ),
                        URIAction(
                            label="冰箱物品查看",
                            uri="http://bit.ly/%E7%9C%8B%E7%9C%8B%E6%9C%89%E4%BB%80%E9%BA%BC",
                        ),
                    ],
                ),
                CarouselColumn(
                    title="仁齋圖書借用登記",
                    altText="我想要讀書！",
                    text="提供需要借用書籍一天以上的齋民登記，以便其他齋民得知書籍流向、以及齋團隊管理。",
                    actions=[
                        URIAction(
                            label="仁齋圖書借用", uri="https://forms.gle/HZ6bjv159QNwCYic6"
                        ),
                        URIAction(
                            label="書籍借用紀錄",
                            uri="https://docs.google.com/spreadsheets/d/1MtcmbiUGx9IZxlr37uwitumMtXcwPamzdTczLQKfMA/edit?usp=sharing",
                        ),
                    ],
                ),
                CarouselColumn(
                    title="T-house 借用登記",
                    altText="我要借齋丘！",
                    text="請先詳閱借用辦法及借用情況後，在填寫表單喔，感謝！如對借用辦法有任何疑問，歡迎私訊齋丘粉專！",
                    actions=[
                        URIAction(
                            label="T-house 借用表單", uri="https://space-64c57.web.app/"
                        ),
                        URIAction(label="T-house 借用狀況", uri="https://lihi1.cc/MdAfJ"),
                    ],
                ),
            ]
        ),
    )
    return tzaiwu_space


def tzaiwu_fix():
    tzaiwu_fix = TemplateSendMessage(
        alt_text="載物書院專屬功能",
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title="報修寢室、浴廁",
                    altText="設備壞壞！",
                    text="「宿舍網路(含網路孔)」相關業務請勿填寫修繕單，由計通中心專人服務(分機：31000)。",
                    actions=[
                        URIAction(
                            label="填寫修繕單",
                            uri="https://sthousing.nthu.edu.tw/DormRF/fillup",
                        )
                    ],
                ),
                CarouselColumn(
                    title="書院公共場地修繕",
                    altText="場地壞壞！",
                    text="仁齋講堂、交誼廳、書房、廚房等公用場地與設備報修",
                    actions=[
                        URIAction(
                            label="清華書院報修系統",
                            uri="https://rcollege.site.nthu.edu.tw/p/423-1103-2549.php?Lang=zh-tw",
                        )
                    ],
                ),
            ]
        ),
    )
    return tzaiwu_fix
