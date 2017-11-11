from bluetool import Bluetooth
from pprint import pprint

bluetooth = Bluetooth()
bluetooth.scan()
devices = bluetooth.get_available_devices()
pprint(devices)
# A8:5C:2C:4F:EB:74
