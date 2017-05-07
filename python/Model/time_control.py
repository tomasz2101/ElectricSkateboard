#!/usr/bin/python
import time
from time import strftime
from datetime import datetime


class ClassTime(object):
    def __init__(self):
        self.time = time.localtime()


# Change date string (format: 2017-04-02 11:31:49)to unix timestamp
# @param string dateString
# @return integer


def get_current_time():
    """

    :return: 
    """
    return strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def get_day():
    return strftime("%Y-%m-%d", time.localtime())


def get_day_time():
    return strftime("%H:%M:%S", time.localtime())


# @param string eg("%Y-%m-%d %H:%M:%S")
def get_time(time_string):
    return strftime(time_string, time.localtime())


def time_to_unix(time_string, pattern='%Y-%m-%d %H:%M:%S'):
    return int(time.mktime(time.strptime(time_string, pattern)))


def unix_to_string(given_time, time_string):
    return datetime.fromtimestamp(int(given_time)).strftime(time_string)


def date_to_unix(date_string=time.localtime()):
    time.mktime(datetime.strptime(date_string, "%d/%m/%Y").timetuple())
