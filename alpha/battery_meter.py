import smbus
import time
from time import gmtime, strftime
from pprint import pprint
import configuration.config_production as config

# Connect Pi 3V3 - VCC, Ground - Ground, SDA - SDA, SCL - SCL.


try:
    pprint(config.BATTERY_METER)
    if config.BATTERY_METER["status"]:
        bus = smbus.SMBus(config.BUS_VERSION)
        # max_voltage = 4.38
        # max_value = 255
        while True:
            print("######################",
                  strftime("%Y-%m-%d %H:%M:%S", gmtime()),
                  "#####################")
            for x in config.BATTERY_METER["modules"]:
                module_adc = config.BATTERY_METER["modules"][x]
                print("address %s" % str(format(module_adc["address"], "02x")))
                pins = []
                for pinNumber in module_adc["pins"]:
                    pinLabel = module_adc["pins"][pinNumber]

                    # pins.append()
                    bus.write_byte(module_adc["address"], pinNumber)
                    value = bus.read_byte(
                        module_adc["address"]) * config.BATTERY_METER[
                                "reference_voltage"] / float(
                        config.BATTERY_METER["max_value"])
                    print("pin %s" % pinLabel, " => %f" % value)
                    # print()
                    # first_input = bus.read_byte(0x48) * max_voltage /
                    #  float(max_value)

                    # bus.write_byte(0x48, 4)
                    # second_input = bus.read_byte(0x48) * max_voltage /
                    # float(max_value)
                    # print(round(first_input, 2), round(second_input, 2))
                    # pprint(pins)
            print("######################    KONIEC   ####################")
            time.sleep(2)
except RuntimeError:
    print("Error battery module")
pass
