import threading
import smbus
import time
from time import gmtime, strftime
from pprint import pprint
import configuration.production as config


class BatteryWatcher(threading.Thread):
    def run(self):
        print('testing connection')
        while True:
            self.check_battery()
            time.sleep(1)

    def check_battery(self):
        try:
            pprint(config.BATTERY_METER)
            if config.BATTERY_METER["status"]:
                bus = smbus.SMBus(config.BUS_VERSION)
                print("######################",
                      strftime("%Y-%m-%d %H:%M:%S", gmtime()),
                      "#####################")
                for _, module_adc in config.BATTERY_METER["modules"].items():
                    print("address %s" % str(
                        format(module_adc["address"], "02x")))
                    for pinNumber, pinLabel in module_adc["pins"].items():
                        bus.write_byte(module_adc["address"],
                                       int(pinNumber))
                        value = bus.read_byte(
                            module_adc["address"]) * config.BATTERY_METER[
                                    "reference_voltage"] / float(
                            config.BATTERY_METER["max_value"])
                        print("pin %s" % pinLabel, " => %f" % value)
                print(
                    "###################    KONIEC   #################")

        except RuntimeError:
            print("Error battery module")


pass
