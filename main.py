#!/usr/bin/python
from models.skateboard import *
import configuration.config_helper as config
from pprint import pprint
import sys

is_debug = "debug" in sys.argv

pprint(config.ENVIRONMENT)


def main():
    message = 'Starting main program'
    if is_debug:
        message += ' with debugging'
    skate = ClassSkateboard()
    if config.ENVIRONMENT == "production":
        skate.connect_wii()
        # Wiimote checker thread
        checker = SkateboardWatcher()
        checker.daemon = True
        checker.start()
    try:
        if config.ENVIRONMENT == "production":
            skate.read_wii_buttons()
        else:
            skate.read_console_input()
    except KeyboardInterrupt:
        raise
    except Exception as e:
        pprint(e)


if __name__ == "__main__":
    main()
