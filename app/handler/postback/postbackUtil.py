"""
這段程式碼定義了一個用於解析 postback 事件的工具包（使用者點擊 Line Bot 的選單或按鈕，而引發的回應事件。）
它包括一段字串，通常是一些鍵值對，用於提供一些額外資訊。
工具包中定義了一個 Param 類別和一個 parse 函數，可以用於將 postback 事件中傳送的字串解析成為一個 Param 物件，並通過訪問其屬性（例如 source、flag 和 info）來獲取相關資訊。
"""

""" 處理 postback event 的工具包 """


class Param:
    def __init__(self, source=None, flag=None, info=None):
        self.source = source
        self.flag = flag
        self.info = info

    def get(self, k):
        if k == "source":
            return self.source
        elif k == "flag":
            return self.flag
        elif k == "info":
            return self.info


def parse(data):
    """解析 postback data
    Params:
        - data string. source=richmenu&flag=epidemic&info=students
    Return:
        - p Param
    """

    param_obj = {"source": "", "flag": "", "info": ""}

    and_split = data.split("&")
    for item in and_split:
        key_value_split = item.split("=")
        k = key_value_split[0]
        v = key_value_split[1]

        param_obj[k] = v

    return Param(param_obj["source"], param_obj["flag"], param_obj["info"])
