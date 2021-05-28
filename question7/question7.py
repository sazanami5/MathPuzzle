# 1964-10-10 ~ 2020-07-24
# 二進数に変換
# に進数を逆に並べる
# 10進数に戻す
#この時元の数字と同じ年を出力

import datetime

startDate = datetime.datetime(1964, 10, 10)
endDate   = datetime.datetime(2020,  7, 24)
beforeDate = startDate + datetime.timedelta(days = 1)

while(True):
    beforeDate = beforeDate + datetime.timedelta(days = 1)
    reversedDate = format(int(beforeDate.strftime("%Y%m%d")),"b")[::-1]
    restoredDate = int(reversedDate, 2)
    if restoredDate == int(beforeDate.strftime("%Y%m%d")):
        print(beforeDate)
    
    if beforeDate == endDate:
        break