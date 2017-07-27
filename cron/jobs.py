# script is running every 1 minute. It checks time and execute proper methods by defined time period
# https://docs.python.org/2/library/time.html#time.struct_time
# link directs to description class of time
import threading
import time
import yaml
from pprint import pprint

threads = []


def print_time_1():
    print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()))
    return True


def execute_thread(method_to_run):
    t = threading.Thread(target=method_to_run)
    threads.append(t)
    t.start()
    return True


if __name__ == "__main__":
    print("start")
    with open('/home/pi/electricSkateboard/python/cron/configuration.yaml', 'r') as f:
        doc = yaml.load(f)
    for job in doc["jobs"]:
        now = time.localtime()
        if job["wday"] == "*" or now.tm_wday in job["wday"]:
            if job["hour"] == "*" or now.tm_hour in job["hour"]:
                if job["minute"] == "*" or now.tm_min in job["minute"]:
                    print(job["name"])
                    execute = execute_thread(eval(str(job["name"])))
                    if execute:
                        print("OK")
                    else:
                        print("Error")
