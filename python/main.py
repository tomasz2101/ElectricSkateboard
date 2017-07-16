#!/usr/bin/python
from Models.skateboard import *
from pprint import pprint
import sys

is_debug = "debug" in sys.argv


def main():
    pprint(is_debug)
    skate = ClassSkateboard()
    skate.connect_wii()
    try:
        skate.run_process()
    except KeyboardInterrupt:
        raise


if __name__ == "__main__":
    main()
