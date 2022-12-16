# elif param.get('info') == 'dyn_search':
#     self.line_bot_api.reply_message(reply_token, busT.dynbus_geton_loc_template())
# elif param.get('flag') == 'dynbus_geton':
#     geton_loc = param.get('info') # 上車地點
#     self.line_bot_api.reply_message(reply_token, busT.dynbus_getoff_loc_template(geton_loc))
# elif param.get('flag') == 'dynbus_getoff':
#     info = param.get('info')
#     info_list = info.split('~')
#     geton_loc = info_list[0] # 上車地點
#     getoff_loc = info_list[1] # 下車地點

#     print('geton_loc:', geton_loc)
#     print('getoff_loc:', getoff_loc)

#     # 判斷 climb||descend(str) 及 line[]
#     direction, line = busUtil.check_direction_and_line(busUtil.BUS_LOC_MAP_EN[geton_loc], busUtil.BUS_LOC_MAP_EN[getoff_loc])

#     print('direction:', direction)
#     print('line:', line)

#     # 現在時間
#     theTime = datetime.now()
#     theTime = theTime.strftime('%H:%M:%S')

#     # request to BusAPI
#     bus = BusAPI()

#     flex_contents = []
#     arriveTime_list = []
#     for l in line:
#         arriveTime, waitTime, err = bus.schedule(theTime, 'campus', direction, l, busUtil.BUS_LOC_MAP_EN[geton_loc])
#         if err:
#             self.line_bot_api.reply_message(reply_token, TextSendMessage(text='動態校車查詢失敗 嗷嗷qq。你可以透過意見回饋讓情報團隊了解情況！'))

#         if arriveTime=='' and waitTime=='':
#             print('此刻沒有班次')
#             break

#         print('arriveTime:', arriveTime)
#         print('waitTime:', waitTime)
#         arriveTime_list.append(arriveTime)

#         dync_bus_flex_content = busT.dync_result_flex_json_content(busUtil.BUS_LOC_MAP_EN[geton_loc], busUtil.BUS_LOC_MAP_EN[getoff_loc], l, arriveTime, waitTime)
#         flex_contents.append(dync_bus_flex_content)

#     # 排序arriveTime, 快的車排前面
#     if len(arriveTime_list) > 1:
#         t0 = datetime.strptime(arriveTime_list[0], '%H:%M:%S')
#         t1 = datetime.strptime(arriveTime_list[1], '%H:%M:%S')

#         if t1 < t0:
#             temp = flex_contents[0]
#             flex_contents[0] = flex_contents[1]
#             flex_contents[1] = temp
#             print('sort flex_contents')

#     if len(flex_contents) == 0:
#         self.line_bot_api.reply_message(reply_token, TextSendMessage(text='此時段沒有班次呦，嗷嗷！'))
#     else:
#         self.line_bot_api.reply_message(reply_token, busT.dync_result_flex_carousel_template(flex_contents))

# elif param.get('flag') == 'stop':
#     if param.get('info') == 'qa':
#         self.line_bot_api.reply_message(reply_token, stopT.stop_qa())
#     if param.get('info') == 'signin':
#         self.line_bot_api.reply_message(reply_token, stopT.cancel_sign())
