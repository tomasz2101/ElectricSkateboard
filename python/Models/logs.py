#!/usr/bin/python
import time
from pathlib import Path
from time import strftime
from datetime import datetime


class ClassLogs(object):
    def __init__(self, log_type, caller_class, notification=False):
        """
        object init 
        :param log_type: (str) name of log type e.g. daily/debug
        :param caller_class: (str) name of calling file or class
        :param notification: (bool) if print notifications
        """
        self.notification = notification
        self.name = self.__class__.__name__
        self.type = log_type
        self.caller = caller_class
        # self.destination = "/media/usb/" + self.type + "_logs/"
        self.fileName = self.type + "_log_" + get_day() + ".txt"
        # self.file = Path(self.destination + self.fileName)
        self.file = Path(self.fileName)

    def log(self, message, notify=False):
        """
        write message to specified file with caller name and time
        :param message: (str) message to write
        :param notify: (bool) if print to command line
        :return :(bool)True 
        """
        message = "%s %s: %s" % (str(get_day_time()), str(self.caller), str(message))
        # noinspection PyTypeChecker
        self.file.open("a").write(u"" + message + "\n")
        if self.notification or notify:
            print(message)
        return True


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
