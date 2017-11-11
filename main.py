#!/usr/bin/python
import models.skateboard as skateboard
import models.battery_meter as battery_meter
import configuration.production as config
from pprint import pprint


def main():
    pprint('Starting main program')
    skate = skateboard.ClassSkateboard(configuration="production")
    if config.ENVIRONMENT == "production":
        skate.connect_wii()
        # Wiimote checker thread
        checker = skateboard.SkateboardWatcher()
        checker.daemon = True
        checker.start()
        battery = battery_meter.BatteryWatcher()
        battery.daemon = True
        battery.start()
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
