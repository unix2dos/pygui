#!/usr/bin/python3

import time
from PyQt5.QtCore import QDate, Qt, QDateTime, QTime


########## QDate
now = QDate.currentDate()
print(now.toString(Qt.ISODate)) # 2019-04-17
print(now.toString(Qt.DefaultLocaleLongDate)) #2019年4月17日
print("Days in month: {0}".format(now.daysInMonth()))#30
print("Days in year: {0}".format(now.daysInYear()))#365



########## QTime
time1 = QTime.currentTime()
print(time1.toString(Qt.DefaultLocaleLongDate)) #GMT+8 10:43:50



########## QDateTime
datetime = QDateTime.currentDateTime()
print(datetime.toString()) #周三 4月 17 10:43:50 2019
print("Local datetime: ", datetime.toString(Qt.ISODate))#Local datetime:  2019-04-17T10:43:50
print("Universal datetime: ", datetime.toUTC().toString(Qt.ISODate))#Universal datetime:  2019-04-17T02:43:50Z
print("The offset from UTC is: {0} seconds".format(datetime.offsetFromUtc()))#The offset from UTC is: 28800 seconds

unix_time = datetime.toSecsSinceEpoch()
print(unix_time) #1555469407
print(time.time()) # sys time 1555469652.958122

d = QDateTime.fromSecsSinceEpoch(unix_time)
print(d.toString(Qt.ISODate)) #2019-04-17T10:50:07
