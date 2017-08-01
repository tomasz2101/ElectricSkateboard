from pathlib import Path
from time import gmtime, strftime
import subprocess

file = Path("/home/pi/logs/log_" + strftime("%Y_%m_%d", gmtime()) + ".txt")


def main():
    log_write(9, "main()")
    try:
        subprocess.call(["sudo", "killall", "pigpiod"])
        subprocess.call(["sudo", "pigpiod"])
        log_write(13, "sudo pigpiod executed")
    except OSError as e:
        debug_write(15, "sudo pigpiod failed: " + str(e))

    try:
        # subprocess.Popen(["sudo", "python", "start_up.py"], stdout=subprocess.PIPE)
        subprocess.call(["sudo", "python", "main.py"], cwd="/home/pi/skateboard")
        log_write(19, "sudo python start_up.py executed")
    except OSError as e:
        debug_write(21, "sudo python start_up.py failed: " + str(e))


def get_time():
    return strftime("%Y-%m-%d %H:%M:%S:", gmtime())


def log_write(line, text):
    file.open("a").write(u"" + get_time() + "|reboot.py|" + str(line) + "|" + text + "\n")


def debug_write(line, text):
    debug = Path("/home/pi/logs/debug_" + strftime("%Y_%m_%d", gmtime()) + ".txt")
    debug.open("a").write(u"" + get_time() + "|reboot.py|" + str(line) + "|" + text + "\n")


main()
