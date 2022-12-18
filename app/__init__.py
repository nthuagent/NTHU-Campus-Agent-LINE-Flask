"""
這段程式碼用來初始化 Flask 應用程式，並設定它的名稱。
然後，它會載入相關的模組，包括 app.views 和 app.linebot，並註冊它們到 Flask 應用程式中。
最後，它會將 gunicorn 的日誌記錄器設定到 Flask 應用程式的日誌記錄器中。這可以讓我們在 Flask 應用程式中也能看到 gunicorn 的日誌記錄。
"""

from flask import Flask
import logging

app = Flask(__name__)

from app.views import base
from app.linebot import callback, followEvent, messageEvent, postbackEvent

# bind gunicon logger to flask_app logger
gunicorn_logger = logging.getLogger("gunicorn.error")
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)
