from time import gmtime, strftime, sleep
from pathlib import Path
import RPi.GPIO as GPIO
import subprocess
# import sys

# sys.path.append('/home/pi/electricSkateboard/models')
import configuration

file = Path("/home/pi/logs/start_up_" +
            strftime("%Y_%m_%d", gmtime()) + ".txt")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(configuration.start_button, GPIO.IN)
GPIO.setup(configuration.ready_led, GPIO.OUT)


def main():
    show_ready_to_work()
    # prev_input = 0
    run_main()
    # while True:
    #     input_button = GPIO.input(configuration.start_button)
    #     if not prev_input and not input_button:
    #         run_main()
    #     prev_input = not input_button
    #     sleep(0.05)


def run_main():
    try:
        subprocess.call(["sudo", "python", "main.py"],
                        cwd="/home/pi/electricSkateboard")
        log_write(32, "python main.py executed")
    except OSError as e:
        debug_write(34, "python main.py: " + str(e))


def get_time():
    return strftime("%Y-%m-%d %H:%M:%S:", gmtime())


def log_write(line, text):
    file.open("a").write(u"" + get_time() +
                         "|start_up.py|" + str(line) + "|" + text + "\n")


def debug_write(line, text):
    debug = Path("/home/pi/logs/debug_" +
                 strftime("%Y_%m_%d", gmtime()) + ".txt")
    debug.open("a").write(u"" + get_time() +
                          "|start_up.py|" + str(line) + "|" + text + "\n")


def show_ready_to_work():
    GPIO.output(18, GPIO.HIGH)


if __name__ == "__main__":
    main()
