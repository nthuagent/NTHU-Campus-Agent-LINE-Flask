""" Chatbot command  """
import os
from modules.affair import qa_engine
import openai

# from revChatGPT.revChatGPT import Chatbot
from linebot.models import *
from app import app
from dotenv import load_dotenv

load_dotenv()


def chatGPT(text):
    if text.startswith("!") or text.startswith("！"):
        text = text[1:]
    openai.api_key = os.environ["OPENAI_TOKEN"]
    ans = openai.Completion.create(
        model="text-davinci-003", prompt=text, max_tokens=1200, temperature=0.7
    )
    return ans["choices"][0]["text"].strip()


"""
config = {
  "session_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..ppUCOk9gixcOjkgT.ngtnqJrwa59XAjK6UU4-GOUG0DWO0afz02V1X12WX43KCAEwclfXTvmRcswB1zu2zFZSmRwmCqs9qAfT5YfecpRa_6hX4JX6TYECYpjAVThu7KRR3KadZHJxBVz1a8jcdjr2p31cLhcMuaCz6MTT9hXERtQvDnAWaTDd-ZyKQ0Jl7ju3dScZZshDVq4XJJ37h7dYgLg0YQU4Wf8amr7IJoh3mAqtMKW29-SkbjQ8g15_wHlRBawPNaqXPUAEfDCsnnNz6GQq2Ffzt2tm3daq1RtJpZsQp-EhO2L9bNacZ_GvZVDVEXRlRF-gpg7OPaXE8HmBKH50P1EQ7YwoRRCJRs7DJ54ZsrW3-M8R6sgDA3wdqZT-l21d4SJKhqqYSnVHLk9EbV27vz78pJBE5mgnwn0Kq5wgSt-zYjLrY6JgLxhv7B7Mt-7ESxS-6u9w3IOT0iJ5G-z-_9pa_FvArdkAX0aaHmOxBJLTklLpd9nAuCHRwBUFYj_BAaXfRvruxIZyHr2UghlObARsThPvLleJ7nms1qwf0GOawjPQZAyQ4-YnWjnWvPKTYrG_F9cfUegH3ITBmyllmS2SPZ5QJvkbykrF-tEJimHJE9sTMk8FBLGL1x__Vdxqzf1LdLA5iiwxMQx6FWq--Eytm019vo3HVGGLw1SeoaGwWMMVmsFml0jH8IwyR5qz1t_YWCj2y4DIarNcNYYXoDkuFLVtFeZP_3yk7x0jdxGdvnyAUZBxE6RfBxlYtnAu0MbYgKD6gP87jHb6sMlTekOzT0cJ8LOTkR6Wln-VpyqW26t3pRDHNl1SmK-KYSR8lRD_vui936w948ut4wCoFu3kGT5NWlgurrV8OTeRbdqlq9ZuGEr01Y1D95BA2rsnM_VtOOz8JNv4b51J9XzXgzj-cSSZjDAF9F_7wPfNGjkrGOvi0h1OV8NXGw_XZ46HttsJm8a-gP3V5LBQ8TCnomiWzXh0XlanRw1ScGWSIiiavnp6hvhZQrLhQBeK_PIUCzlDLw8rELbQiGeSK2D7qhPEEnm7NcgfW52eF5hpHhq1URCn7I3dU-EXjpA6UE3vhsO83KSYU-tnqItv6L6IkgoEE0Ipeqv_9JwLxOmrE9zYSgSmgDAic1fhpCCeGg0p5uPBL7_eBFgsBZdiwC031baDCWkUvyhs9z9pVlcVUC_WYJZVhoEV4NfiOQGKRDdYIkR6TuoOFCgllFKJObF4BV94t8U25ic9Wla7zKjqCo2QaCw-aB0APpSaMy-dzziEEWarpgBwz71EXmQ-pPXfqZGLtA43wFe1wSzCI3_J9QICpLWt8YxZ6dSCSsZcOkOLqx3SjbUQR0ktQfh5rRbqEwqmkIXc52ON08F10nSlHQ_3sHdfs_ZLZKsp7nzNedcSEn834bZRRQF5AWjDK631DvyevhyPgyPZarcFvZ9yCki04TEsrvhzfaTmzqoss3ISS6VlRUOr6ECXKUasHwHYu_s5rCWiusvq8cth6Ef80vapbFyxCEryEt1J0VFZlOh2ivocVB3sKlMJ3iq7gE0vRKaooIg7YkAG3d7_mmpMOyff1H2n4VzoOp5jp1jSu1k1H5mw1bt3yKRys8_8Sqv9bHwfmvc4PVNYIkdZoqaLENhhaoa6x3rvXPwfEd6nyUfpaqVVfRmiwZeXlvvI_JjiYW6Gac-ncIYwihmk2sWR_fQNTFrrYxEwRGCu_A5OK7rQdLq8pEJ23j5nAfCc9LSfxWbwhmw6fkInLWN2wEKDRg8bzlZsLk05II8Lc-LMxh2Zes8aWKJT1rJkAr5007JQD2SaDwvLReitJNZqlsspK4mnY20P3PBbma5bqo2XQaiA49qJFLhD7cCEh3nHQ6kq6jLWqzbrI_NR96B2lLzn7Oexd9lmBTh3CQi5TNyNckOIu8lLiTBSVrH4_GwTETLcBQOn1nVLlzVzmehK8Nd7AEO_ISE3uUlPPBxG4nPTnaLizpubU8Ht115CimPoEUVnrZsEoT2ymDqUBApLMQF97GpZh3r21I2UvJfNpHeqikVU9u_d89KzotninL7rfanBCNYmKzfhoRKCNK7RTdqpIZm2AZ_E_taP7FEh_yuDe-m3e4aN2mlpumqOcJpAu-8o3hEFJlsPUhuMeUwHymWt0wGkkiuSCA-R8vyYCIDql1V-z537JuHxAsnEN20Sur1YQRVJm7z2OsfidTUESxBiWJaR1NFCeqelViUFyMtHK6I0FH-Sdu83jW8oKCg02M-Aft8eoF-SO2rx57Qd0xxAuQ.fAifGP8UMx_K33RGUZkMPQ",
  "cf_clearance": "MUvYHCVmFoZpYJRZzTYcGXqZj99m0ud72pdSCP.scxs-1670846519-0-160",
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46",
  #"proxy": "<HTTP/HTTPS_PROXY>"
}

chatbot = Chatbot(config, conversation_id=None)
"""


class CmdHandler:
    def __init__(self, line_bot_api, user_instance):
        self.line_bot_api = line_bot_api
        self.user = user_instance

    def detect(self, msg):
        """判斷是否為chatbot command
        Params:
            - msg
        Return:
            - isCMD(bool): 若!在第一個字元
        """

        if msg.startswith("!") or msg.startswith("！"):
            return True
        else:
            return False

    def extract_msg(self, msg):
        if msg[0] == "!":
            return msg.split("!")[1]
        elif msg[0] == "！":
            return msg.split("！")[1]

    def run(self, event, msg):
        # intro all cmd of chatbot
        if msg == "!" or msg == "！":
            self.line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text="在你要打的句子面前加上驚嘆號 (！)，就能召喚神奇海螺囉")
            )
        # 執行 cmd
        else:
            # user_message = event.message.text
            # print(user_message)
            # response = chatbot.get_chat_response((user_message), output="text")
            # print(response)
            # Get opengpt's response
            # openai_response = response["message"]
            self.line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=chatGPT(event.message.text))
            )


"""
usage:
elif event.message.text!='你絕對不會輸入這個文字':
     line_bot_api.reply_message(  # 回復傳入的訊息文字
     event.reply_token,
     TextSendMessage(text=chatGPT(event.message.text))
     )
"""
