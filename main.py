#!/usr/bin/python
from Models.skateboard import *
from pprint import pprint
import sys

is_debug = "debug" in sys.argv


def main():
    message = 'Starting main program'
    if is_debug:
        message += ' with debugging'
    print(message)
    skate = ClassSkateboard()
    skate.connect_wii()

    # Wiimote checker thread
    checker = SkateboardWatcher()
    checker.daemon = True
    checker.start()
    try:
        skate.run_process()
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
