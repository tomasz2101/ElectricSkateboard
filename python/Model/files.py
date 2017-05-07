#!/usr/bin/python
from logs import *
import json
from pathlib import Path


class ClassFiles(object):
    def __init__(self, destination, notification=False):
        self.name = self.__class__.__name__
        self.debug = ClassLogs("debug", self.name)
        self.destination = destination
        self.notification = notification
        self.file = Path(self.destination)
        self.permission = "a"

    def file_exists(self):
        """
        check if a file exists
        :return: (bool) flag
        """
        flag = self.file.is_file()
        if self.notification:
            if flag:
                print self.name + ": File " + self.name + "doesn't exist"
            else:
                print self.name + ": File " + self.name + "exists"
        return flag

    def create_new(self):
        """
        create new file
        :return: (bool)
        """
        self.file.open("w")
        flag = self.file.is_file()
        if self.notification:
            if flag:
                print self.name + ": File " + self.destination + "created"
            else:
                print self.name + ": File " + self.destination + "creation failed"
        return flag

    def write(self, message):
        """
        write message to file
        :param message: (str)
        :return: (bool)
        """
        flag = self.file_exists()
        if flag:
            # noinspection PyTypeChecker
            self.file.open(self.permission).write(u"" + message + "\n")
        else:
            print self.name + ": Trying to write message into empty file" + self.destination
        return flag

    def read_json_file(self):
        """
        read json file
        :return: (object)
        """
        object_from_file = {}
        if self.file_exists:
            with self.file.open() as dataFile:
                try:
                    object_from_file = json.load(dataFile)
                except IOError:
                    print "file " + self.destination + " is not json file"
        else:
            # send notification to domoticz server about missing file
            print "file " + self.destination + " doesnt exist"
        return object_from_file

    def save_json_file(self, object_to_save):
        """
        save json object to file
        :param object_to_save: (object)
        """
        try:
            json_object = json.dumps(object_to_save)
            # noinspection PyTypeChecker
            self.file.open("w").write(u"" + json_object)
        except IOError:
            print "error"

    def create_empty_json_file(self):
        """
        create empty json file
        """
        empty_json_file = {
            1: {
                "id": 1,
                "Status": "On"
            }
        }
        empty_json_file = json.dumps(empty_json_file)
        # noinspection PyTypeChecker
        self.file.open("w").write(u"" + empty_json_file)
