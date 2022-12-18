"""
查詢校園電話簿。
它包含了三個類別：Phone_Engine、DataAPI和PhoneAPI。
Phone_Engine類別中包含了一些函式，用於處理查詢的流程。
DataAPI和PhoneAPI則是用於從資料庫中讀取資料的類別。
phone_list_loader函式則是用於讀取電話簿資料的輔助函式。
程式碼執行流程如下：
使用者輸入查詢的資訊，如「清華大學校長室電話」。
透過Phone_Engine類別的match_ans函式，與電話簿資料進行比對。
如果比對到答案，則回傳相對應的電話號碼；如果沒有比對到答案，則回傳預設的錯誤訊息。
"""

from fuzzywuzzy import fuzz, process

from .loader import phone_list_loader


class Phone_Engine:
    def __init__(self):
        pass

    def load_data(self):
        self.data = phone_list_loader()

    def _get_data_ques_list(self):
        ques_list = []
        for qa in self.data:
            ques_list.append(qa["name"])

        return ques_list

    def _get_index_of_ques(self, q):
        for idx, qa in enumerate(self.data):
            if qa["name"] == q:
                return idx

    def _get_ans(self, q):
        q_idx = self._get_index_of_ques(q)
        return self.data[q_idx]["name"], self.data[q_idx]["phone"]

    def match_ans(self, q):
        ques_list = self._get_data_ques_list()
        result = process.extractOne(
            q, ques_list, scorer=fuzz.token_sort_ratio, score_cutoff=5
        )

        name = None
        phone = None
        none_msg = None

        if result == None:
            none_msg = (
                """汪汪，目前找不到答案，如有我們沒有捕捉到的資訊。你可以到「神奇海螺」→「問題回饋」新增你想詢的問題，我們會盡快找到答案！"""
            )
            return name, phone, none_msg
        else:
            name, phone = self._get_ans(result[0])
            return name, phone, none_msg
