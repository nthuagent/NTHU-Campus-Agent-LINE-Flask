"""
定義一個名為 QA_Engine 的類別，其中有四個函式：

__init__：初始化函式。
load_data：載入問答資料。
_get_data_ques_list：回傳資料中的所有問題。
_get_index_of_ques：回傳問題在資料中的索引值。
_get_ans：回傳某問題的答案。
match_ans：比對輸入問題與資料中的問題，並回傳最匹配的問題的答案。
此類別使用到了 fuzzywuzzy 套件的 token_sort_ratio 方法，該方法可以用來比對兩個字串的相似程度。此類別也會使用到一個 data_loader 函式，用來從外部載入問答資料。

可以透過呼叫 QA_Engine 類別的實例，並使用 load_data 函式來載入資料，再使用 match_ans 函式來比對輸入的問題，以回傳最匹配的答案（模糊搜尋）。
"""

from fuzzywuzzy import fuzz, process

from .loader import data_loader


class QA_Engine:
    def __init__(self):
        pass

    def load_data(self, category):
        self.data = data_loader(category)

    def _get_data_ques_list(self):
        ques_list = []
        for qa in self.data:
            ques_list.append(qa["ques"])

        return ques_list

    def _get_index_of_ques(self, q):
        for idx, qa in enumerate(self.data):
            if qa["ques"] == q:
                return idx

    def _get_ans(self, q):
        q_idx = self._get_index_of_ques(q)
        return self.data[q_idx]["ans"]

    def match_ans(self, q):
        ques_list = self._get_data_ques_list()
        result = process.extractOne(
            q, ques_list, scorer=fuzz.token_sort_ratio, score_cutoff=5
        )

        if result == None:
            none_msg = (
                """汪汪，說目前找不到答案，如有我們沒有捕捉到的資訊。你可以到「神奇海螺」→「問題回饋」新增你想詢的問題，我們會盡快找到答案！"""
            )
            return none_msg
        else:
            ans = self._get_ans(result[0])
            return ans
