"""
建立伺服器後，測試用
這段程式碼是在建立一個Flask伺服器，並定義了兩個路由。
第一個路由 /，當使用者瀏覽根目錄時，就會回傳 "Hi there, this is NTHU LINE Flask"。
第二個路由 /ping，當使用者瀏覽/ping時，也會回傳 "Hi there, this is NTHU LINE Flask"。
這樣的設定可以用來測試伺服器的狀態，並且回應使用者的請求。
"""

from app import app


@app.route("/", methods=["GET"])
def home():
    return "Hi there, this is NTHU LINE Flask"


@app.route("/ping", methods=["GET"])
def ping():
    return "Hi there, this is NTHU LINE Flask"
