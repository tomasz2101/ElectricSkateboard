import smbus
import time
from time import gmtime, strftime
from pprint import pprint
import configuration.production as config

# Connect Pi 3V3 - VCC, Ground - Ground, SDA - SDA, SCL - SCL.


try:
    pprint(config.BATTERY_METER)
    if config.BATTERY_METER["status"]:
        bus = smbus.SMBus(config.BUS_VERSION)
        while True:
            print("######################",
                  strftime("%Y-%m-%d %H:%M:%S", gmtime()),
                  "#####################")
            for _, module_adc in config.BATTERY_METER["modules"]:
                print("address %s" % str(format(module_adc["address"], "02x")))
                pins = []
                for pinLabel, pinNumber in module_adc["pins"]:
                    bus.write_byte(module_adc["address"], int(pinNumber))
                    value = bus.read_byte(
                        module_adc["address"]) * config.BATTERY_METER[
                                "reference_voltage"] / float(
                        config.BATTERY_METER["max_value"])
                    print("pin %s" % pinLabel, " => %f" % value)
            print("######################    KONIEC   ####################")
            time.sleep(2)
except RuntimeError:
    print("Error battery module")
pass
