import RPi.GPIO as GPIO
import configuration.production as config


class ClassLed:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(config.LED_STRIP["pin_blue"], GPIO.OUT)
        GPIO.setup(config.LED_STRIP["pin_red"], GPIO.OUT)
        GPIO.setup(config.LED_STRIP["pin_green"], GPIO.OUT)

        self.blue = GPIO.PWM(config.LED_STRIP["pin_blue"],
                             config.LED_STRIP["frequency_hz"])
        self.red = GPIO.PWM(config.LED_STRIP["pin_blue"],
                            config.LED_STRIP["frequency_hz"])
        self.green = GPIO.PWM(config.LED_STRIP["pin_blue"],
                              config.LED_STRIP["frequency_hz"])

        self.blue.start(0)
        self.red.start(0)
        self.green.start(0)
        self.status = {
            "blue": 0,
            "green": 0,
            "red": 0,
        }

    @staticmethod
    def set_led(led, value):
        try:
            value = int(value)
            if value > config.LED_STRIP["max_pwm"]:
                raise ValueError('PWM value exceed max possible')
            led.ChangeDutyCycle(value)
            return value
        except ValueError:
            led.ChangeDutyCycle(0)
            return 0

    def set_blue(self, value):
        self.set_led(led=self.blue, value=value)
        self.status["blue"] = value

    def set_green(self, value):
        self.set_led(led=self.green, value=value)
        self.status["green"] = value

    def set_red(self, value):
        self.set_led(led=self.red, value=value)
        self.status["red"] = value

    def increase_green(self):
        try:
            self.set_led(led=self.green, value=int(self.status["green"]) + 1)
        except ValueError:
            self.set_led(led=self.green, value=0)

    def decrease_green(self):
        try:
            self.set_led(led=self.green, value=int(self.status["green"]) - 1)
        except ValueError:
            self.set_led(led=self.green, value=0)
