#!/usr/bin/python3
import configuration.skateboard as config_helper
from pprint import pprint


def test_configuration():
    pprint(config_helper.configuration)


if __name__ == '__main__':
    test_configuration()
