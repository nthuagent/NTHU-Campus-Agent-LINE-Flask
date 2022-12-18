"""
這段程式碼定義了一個函數，用於對傳入的地點名稱進行對應並返回其地址、經緯度等相關資訊。
這些資訊可能會用於地圖或導航應用程式。如果傳入的地點名稱不存在，函數會將其設置為空字串並返回。
"""


data = {
    "研發大樓": [24.795331, 120.997054],
    "創新育成中心": [24.795236, 120.996590],
    "工程一館": [24.795094, 120.996176],
    "工一": [24.795094, 120.996176],
    "科儀中心": [24.794479, 120.996259],
    "化學館": [24.796424, 120.995975],
    "動機化學實驗室": [24.796772, 120.995355],
    "化工館": [24.796396, 120.995007],
    "學習資源中心": [24.795523, 120.994670],
    "旺宏館": [24.795523, 120.994670],
    "行政中心": [24.795523, 120.994670],
    "國際會議廳": [24.795523, 120.994670],
    "藝術創新中心": [24.795523, 120.994670],
    "亞洲政策中心": [24.795523, 120.994670],
    "斯麥爾咖啡": [24.795523, 120.994670],
    "圖書館": [24.795523, 120.994670],
    "採編組": [24.795523, 120.994670],
    "資訊系統組": [24.795523, 120.994670],
    "典閱組": [24.795523, 120.994670],
    "服務與創新組": [24.795523, 120.994670],
    "綜合館務組": [24.795523, 120.994670],
    "特藏組": [24.795523, 120.994670],
    "秘書處": [24.795523, 120.994670],
    "教育館": [24.795727, 120.993952],
    "師資培育中心": [24.795727, 120.993952],
    "通識教育中心": [24.795727, 120.993952],
    "共同教育委員會": [24.795727, 120.993952],
    "華德福教育中心": [24.795727, 120.993952],
    "第一綜合大樓": [24.794765, 120.994444],
    "綜一": [24.794765, 120.994444],
    "行政大樓": [24.794765, 120.994444],
    "綜合學務組": [24.794765, 120.994444],
    "學務處": [24.794765, 120.994444],
    "總務處": [24.794765, 120.994444],
    "全球事務處": [24.794765, 120.994444],
    "招生組": [24.794765, 120.994444],
    "註冊組": [24.794765, 120.994444],
    "人事室": [24.794765, 120.994444],
    "主計室": [24.794765, 120.994444],
    "研究發展處": [24.794765, 120.994444],
    "校園規劃組": [24.794765, 120.994444],
    "綜合企劃組": [24.794765, 120.994444],
    "計畫管理組": [24.794765, 120.994444],
    "事務組": [24.794765, 120.994444],
    "保管組": [24.794765, 120.994444],
    "採購組": [24.794765, 120.994444],
    "文書組": [24.794765, 120.994444],
    "出納組": [24.794765, 120.994444],
    "營繕組": [24.794765, 120.994444],
    "教務處": [24.794765, 120.994444],
    "第二綜合大樓": [24.794308, 120.993361],
    "綜二": [24.794308, 120.993361],
    "藝術中心": [24.794308, 120.993361],
    "計算機與通訊中心": [24.794308, 120.993361],
    "會議廳": [24.794308, 120.993361],
    "校務資訊組": [24.794308, 120.993361],
    "網路系統組": [24.794308, 120.993361],
    "學習科技組": [24.794308, 120.993361],
    "第三綜合大樓": [24.794931, 120.993404],
    "綜三": [24.794931, 120.993404],
    "工程三館": [24.796418, 120.992671],
    "工三": [24.796418, 120.992671],
    "材料科技館": [24.796545, 120.991807],
    "材料實驗館": [24.796556, 120.990883],
    "合金實驗館": [24.796685, 120.990180],
    "台達館": [24.795998, 120.992134],
    "資訊電機館": [24.794943, 120.992145],
    "資電館": [24.794943, 120.992145],
    "數學圖書館": [24.794943, 120.992145],
    "物理館": [24.794183, 120.992370],
    "物理圖書分館": [24.794183, 120.992370],
    "工科館": [24.790958, 120.990893],
    "綠色低碳能源教學研究大樓": [24.790746, 120.991351],
    "李存敏館": [24.790746, 120.991351],
    "綠能大樓": [24.790746, 120.991351],
    "綠能館": [24.790746, 120.991351],
    "原子爐": [24.789893, 120.992099],
    "同位素館": [24.789240, 120.992317],
    "加速器館": [24.788835, 120.992271],
    "高能光電實驗室": [24.788704, 120.991853],
    "生物科技館": [24.789701, 120.991151],
    "生醫工程與環境科學館": [24.789202, 120.991274],
    "生命科學一館": [24.789779, 120.990391],
    "生命科學二館": [24.789285, 120.989778],
    "人文社會學館": [24.790031, 120.989070],
    "人文社會學院": [24.790031, 120.989070],
    "人社院": [24.790031, 120.989070],
    "台積館": [24.786815, 120.988265],
    "科技管理學院": [24.786815, 120.988265],
    "創新育成大樓": [24.786239, 120.988760],
    "國際產學營運總中心": [24.786239, 120.988760],
    "行政組": [24.786239, 120.988760],
    "產學企劃組": [24.786239, 120.988760],
    "智財技轉組": [24.786239, 120.988760],
    "技轉中心": [24.786239, 120.988760],
    "清華實驗室": [24.785724, 120.989839],
    "醫輔大樓": [24.796307, 120.994396],
    "郵局": [24.795638, 120.997007],
    "清華大草坪": [24.793923, 120.993054],
    "水漾餐廳": [24.794095, 120.993356],
    "大禮堂": [24.793379, 120.993839],
    "社團辦公室": [24.793023, 120.994142],
    "水木生活中心": [24.792239, 120.994365],
    "學生住宿組": [24.792239, 120.994365],
    "生活輔導組": [24.792239, 120.994365],
    "水木餐廳": [24.792271, 120.994345],
    "水木書苑": [24.792364, 120.994656],
    "風雲樓": [24.792066, 120.994743],
    "小吃部": [24.793194, 120.993083],
    "麥當勞": [24.793194, 120.993083],
    "統一超商": [24.793194, 120.993083],
    "711": [24.793194, 120.993083],
    "室內網球場": [24.796371, 120.990364],
    "游泳池": [24.794929, 120.991487],
    "舊體育館": [24.794267, 120.991565],
    "桌球館": [24.794267, 120.991565],
    "體育館": [24.793562, 120.991667],
    "體育室": [24.793562, 120.991667],
    "蒙民偉樓": [24.793656, 120.992071],
    "學生活動中心": [24.793656, 120.992071],
    "課外活動組": [24.793656, 120.992071],
    "駐警隊": [24.791579, 120.991832],
    "土地公廟": [24.787417, 120.990924],
    "校友體育館": [24.795336, 120.989802],
    "自強樓": [24.796958, 120.991888],
    "西院宿舍": [24.797500, 120.991722],
    "莊敬樓": [24.797304, 120.990759],
    "第二招待所": [24.797080, 120.991218],
    "教職員單身宿舍": [24.797905, 120.991342],
    "清華會館": [24.797998, 120.991082],
    "東院宿舍": [24.794698, 120.997451],
    "學人宿舍": [24.790161, 120.998310],
    "碩齋": [24.791243, 120.996792],
    "信齋": [24.790876, 120.995779],
    "禮齋": [24.791056, 120.995406],
    "仁齋": [24.791448, 120.995755],
    "實齋": [24.791477, 120.995173],
    "實齋交誼廳": [24.791592, 120.994768],
    "華齋": [24.791721, 120.994135],
    "誠齋": [24.791355, 120.994012],
    "義齋": [24.790982, 120.993993],
    "鴻齋": [24.790487, 120.993819],
    "學齋": [24.789987, 120.993089],
    "明齋": [24.792692, 120.993147],
    "平齋": [24.792534, 120.993260],
    "善齋": [24.792069, 120.993504],
    "新齋": [24.791757, 120.992784],
    "清齋": [24.790951, 120.993441],
    "雅齋": [24.792790, 120.991919],
    "靜齋": [24.792518, 120.991340],
    "慧齋": [24.792136, 120.991276],
    "文齋": [24.792007, 120.990847],
    "女宿": [24.792479, 120.991892],
    "立體機車停車場": [24.797310, 120.995583],
    "機車塔": [24.797310, 120.995583],
    "北校區實驗室廢水處理廠": [24.796810, 120.992503],
    "電工房": [24.792843, 120.992679],
    "清交小徑": [24.790607, 120.995653],
    "室外排球場": [24.793916, 120.990957],
    "田徑場": [24.794126, 120.990020],
    "操場": [24.794126, 120.990020],
    "游泳池": [24.794963, 120.991483],
    "棒球場": [24.796049, 120.990807],
    "網球場": [24.796370, 120.989863],
    "醫輔中心": [24.796370, 120.994380],
    "衛生保健組": [24.796370, 120.994380],
    "諮詢中心": [24.796370, 120.994380],
    "診所": [24.795730, 120.996922],
    "清華大學附設診所": [24.795730, 120.996922],
    "附設診所": [24.795730, 120.996922],
    "奕園停車場": [24.788315, 120.991918],
    "奕園": [24.787872, 120.990715],
    "梅園": [24.792371, 120.990010],
    "合勤演藝中心": [24.794669, 120.994415],
    "成功湖": [24.793493, 120.995342],
    "大草皮": [24.795433, 120.995564],
    "北校門口": [24.796607, 120.997033],
    "北校門": [24.796607, 120.997033],
    "南校門口": [24.786080, 120.988363],
    "南校門": [24.786080, 120.988363],
    "蝴蝶園": [24.790629, 120.988586],
    "全家": [24.792249, 120.994236],
    "全家便利商店": [24.792249, 120.994236],
    "荷塘": [24.790613, 120.992277],
    "客運站": [24.795669, 120.998127],
    "火車站": [24.801602, 120.971597],
    "新竹火車站": [24.801602, 120.971597],
    "馬偕醫院": [24.800374, 120.990775],
    "醫院": [24.800374, 120.990775],
    # 南大校區
    "計通中心": [24.792841, 120.966480],
    "推廣教育大樓": [24.792841, 120.966480],
    "校使館": [24.793892, 120.965863],
    "圖書館南大分館": [24.794182, 120.965478],
    "南大圖書館": [24.794182, 120.965478],
    "教學大樓": [24.793782, 120.965108],
    "通識中心": [24.793782, 120.965108],
    "教與學中心": [24.793782, 120.965108],
    "綜合教育大樓": [24.793784, 120.965097],
    "資源教室": [24.793784, 120.965097],
    "迎曦軒": [24.793874, 120.964091],
    "崇善樓": [24.793699, 120.963933],
    "鳴鳳樓": [24.793463, 120.963753],
    "諮商中心": [24.793463, 120.963753],
    "原資中心": [24.793463, 120.963753],
    "衛保組": [24.793463, 120.963753],
    "學務處聯合辦公室": [24.793463, 120.963753],
    "綜合體育館": [24.792898, 120.963626],
    "體育健康教學大樓": [24.792952, 120.963163],
    "學生第二活動中心": [24.792587, 120.963238],
    "樹德樓": [24.792356, 120.963391],
    "掬月齋": [24.792125, 120.963447],
    "音樂二館": [24.792349, 120.964208],
    "運動場": [24.792690, 120.965246],
    "南大校區正門": [24.792349, 120.964208],
    "南大校門": [24.792349, 120.964208],
    "南大正門": [24.792349, 120.964208],
    "南大校門口": [24.792349, 120.964208],
}


def mapping(location):
    latitude = data.get(location, None)[0]
    longitude = data.get(location, None)[1]
    exist = True if latitude else False

    # return map information
    mapInfo = {
        "isExist": exist,
        "info": {
            "title": location,
            "address": location,
            "latitude": latitude,
            "longitude": longitude,
        },
        "errMsg": None,
    }

    if not exist:
        mapInfo[
            "errMsg"
        ] = "汪汪，我聽不懂還在學習中。你可以到「選單」→「神奇海螺」→「問題反饋」教我。如果還想再問我問題可以回到「選單」再問一次喔！"

    return mapInfo
