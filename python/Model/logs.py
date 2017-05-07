#!/usr/bin/python

from time_control import *
from pathlib import Path


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
        self.destination = "/media/usb/" + self.type + "_logs/"
        self.fileName = self.type + "_log_" + get_day() + ".txt"
        self.file = Path(self.destination + self.fileName)

    @staticmethod
    def test():
        print"nothing"

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
            print message
        return True
