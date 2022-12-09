# NTHU-LINE-Flask

> The LINE server which handles users' messages from LINE client based on Python flask



# Get Stated

* Run it in the developing mode

  ~~~cmd
  python3 run.py
  ~~~

* Run it in the production mode

  ~~~cmd
  gunicorn app:app -c ./gunicorn.conf.py
  ~~~

# Env
            - name: LINE_OFFICIAL_TOKEN 
              valueFrom: 
                secretKeyRef:
                  name: line-official-token # kubernetes secret
                  key: password
            - name: LINE_WEBHOOK_STRING 
              valueFrom: 
                secretKeyRef:
                  name: line-webhook-string # kubernetes secret
                  key: password
            - name: GINIP
              valueFrom:
                configMapKeyRef:
                  name: gin-config
                  key: ginip


# Feactures

All linebot's event handler is implemented in  `app/linebot`. There are four programs to handle the different events.

1. `callback.py`：Handle all post requests come from `/callback`.
2. `followEvent.py`：Handle the event that new user add NTHU LINE Chatbot.
3. `messageEvent.py`：The chatbot core program. Process the message sends by user and will reply proper message to the user.

4. `postbackEvent.py`：Handle the postback event.



# Docker & Kubernetes

Please refer to **Dockerfile** and **gke folder**



# License

Developed by **Jenson Su** & **Jonathan Wu**

# Code Location
Bus templates:
/blob/master/app/handler/richmenu/template/busT.py

# Flag status

|    Flag status    |   Description    |
| :---------------: | :--------------: |
|       init        |    無互動狀態    |
|    andx_insert    |   處理新增笑話   |
|      affair       |   處理校務詢問   |
|     feedback      |   處理問題回饋   |
| epidemic_feedback | 處理疫情意見回饋 |
|      mapping      |   處理地圖查詢   |
