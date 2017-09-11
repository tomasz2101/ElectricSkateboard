#!/usr/bin/python
from models.skateboard import *
from pprint import pprint
import sys

is_debug = "debug" in sys.argv


def main():
    message = 'Starting main program'
    if is_debug:
        message += ' with debugging'
    print(message)
    skate = ClassSkateboard()
    if configuration["environment"]["status"] == "production":
        skate.connect_wii()
        # Wiimote checker thread
        checker = SkateboardWatcher()
        checker.daemon = True
        checker.start()
    try:
        if configuration["environment"]["status"] == "production":
            skate.read_wii_buttons()
        else:
            skate.read_console_input()
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
