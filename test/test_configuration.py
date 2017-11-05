#!/usr/bin/python3
import configuration.config_helper as config_helper
from pprint import pprint


def test_configuration():
    pprint(config_helper.MOTOR)


if __name__ == '__main__':
    test_configuration()
