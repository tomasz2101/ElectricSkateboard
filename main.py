#!/usr/bin/python
from models.skateboard import *
import configuration.config_helper as config
from pprint import pprint
import sys

is_debug = "debug" in sys.argv


def main():
    pprint('Starting main program')
    skateboard = ClassSkateboard()
    if config.ENVIRONMENT == "production":
        skateboard.connect_wii()
        # Wiimote checker thread
        checker = SkateboardWatcher()
        checker.daemon = True
        checker.start()
    try:
        if config.ENVIRONMENT == "production":
            skateboard.read_wii_buttons()
        else:
            skateboard.read_console_input()
    except KeyboardInterrupt:
        raise
    except Exception as e:
        pprint(e)


if __name__ == "__main__":
    main()
