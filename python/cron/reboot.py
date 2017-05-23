import subprocess
import sys
sys.path.append('..')
from Models.files import *
subprocess.Popen("sudo mount -t vfat -o uid=pi,gid=pi /dev/sda1 /media/usb", shell=True, stdout=subprocess.PIPE)

debug = ClassLogs("cron", "Reboot")
debug.log("Execute main program")
