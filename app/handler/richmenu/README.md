# richmenu
此處放著主選單的程式碼，進入點在 `__init__.RichmenuHandler.run`，會判斷選到哪一項
- 公車: `template/busT.py` 回傳公車列表
- 地圖: 去 `utils.locationUtil` 抓地點
- 防疫Q&A: 不在 menu 上
- 切換主動推播、關閉主動推播、開啟主動推播: 調整推播設定，一般來說不需更動
- 校務專區: `template/affairT.py` 回傳校務資訊
- 哈哈: 不在 menu 上
- 清華校內工讀: 去 `utils.schoolRecruitUtil` 爬資料