'''
工讀機會查看。這段程式碼會從指定的網站爬取資料，並將爬取到的資料存入 data 這個清單中。
'''

import requests
import requests.packages.urllib3
from pyquery import PyQuery
requests.packages.urllib3.disable_warnings() #關閉警告
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'
BULLETIN_URL = 'https://bulletin.site.nthu.edu.tw/p/403-1086-5075-1.php?Lang=zh-tw'

def get_list():
    data = []
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    html = requests.get(BULLETIN_URL, headers=headers, verify=False)

    dom = PyQuery(html.content)
    recruitments = dom('#pageptlist .listBS').items()

    for item in recruitments:
        date = item('.mdate.before').text()

        url_dom = item('a')
        title = url_dom.text()
        url = url_dom.attr.href

        data.append({
            'date': date,
            'title': title,
            'url': url
        })

    return data