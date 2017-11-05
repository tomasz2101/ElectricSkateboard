import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 500)  # channel=18 frequency=50Hz
p.start(0)
try:
    while 1:
        name = input("PWM")
        p.ChangeDutyCycle(int(name))
except KeyboardInterrupt:
    pass
p.ChangeDutyCycle(0)
# p.stop()
# GPIO.cleanup()
