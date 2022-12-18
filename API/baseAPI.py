import os
from dotenv import load_dotenv
import requests

load_dotenv()


class API:
    def __init__(self):
        self.URL = os.environ["GINIP"] + "/api/v1"
        # self.URL = 'http://127.0.0.1:5000/api/v1'
        self.liff_URL = os.environ["GINIP"] + "/api/v1"

    def ping(self):
        url = self.URL + "/ping"

        try:
            r = requests.get(url).json()

            if r.status_code == 200:
                print(r["msg"])
        except:
            print("ping error")
