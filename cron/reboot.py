from pathlib import Path
from time import gmtime, strftime
import subprocess
import configuration.config_production as config

# from pprint import pprint
# pprint(configuration)

file = Path(config.LOGGING_DIRECTORY + "/cron_" +
            strftime("%Y_%m_%d", gmtime()) + ".txt")


def main():
    # log_write(12, "Starting " + configuration["environment"] + " mode.")
    try:
        subprocess.call(["sudo", "killall", "pigpiod"])
        subprocess.call(["sudo", "pigpiod"])
        # log_write(16, "sudo pigpiod executed")
    except OSError as e:
        debug_write(18, "sudo pigpiod failed: (" +
                    config.ENVIRONMENT + ") " + str(e))
    try:
        subprocess.call(["python", "main.py"], cwd=config.PROGRAM_DIRECTORY)
        # log_write(21, "sudo python start_up.py executed")
    except OSError as e:
        debug_write(23, "sudo python start_up.py failed: " + str(e))


def get_time():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())


def log_write(line, text):
    file.open("a").write(u"" + get_time() +
                         "|reboot.py|" + str(line) + "|" + text + "\n")


def debug_write(line, text):
    debug = Path(config.LOGGING_DIRECTORY + "/debug_" +
                 strftime("%Y_%m_%d", gmtime()) + ".txt")
    debug.open("a").write(u"" + get_time() +
                          "|reboot.py|" + str(line) + "|" + text + "\n")


if __name__ == "__main__":
    main()
