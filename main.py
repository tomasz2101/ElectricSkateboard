#!/usr/bin/python
import models.skateboard as skateboard
import models.battery_meter as battery_meter
import configuration.production as config
from pprint import pprint


def main():
    """
    Main function responsible for:
    - init all electric skateboard components
    - init battery meter
    - init connection with wii remote over bluetooth
    :return:
    """
    skate = skateboard.ClassSkateboard(configuration="production")
    if config.ENVIRONMENT == "production":
        battery = battery_meter.BatteryWatcher()
        battery.daemon = True
        battery.start()

        skate.connect_wii()
        # Wiimote checker thread
        checker = skateboard.SkateboardWatcher()
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
