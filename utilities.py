__author__ = 'J08M'
import datetime

def getTimeMinutes():
    current_time = datetime.datetime.now().time()
    time_str = str(current_time.hour) + ":"
    if current_time.minute < 10:
        time_str += "0"
    time_str += str(current_time.minute)
    return time_str



