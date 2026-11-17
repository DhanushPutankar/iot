#Binary counter using LEDs

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pins = [18, 23, 24, 25]

for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        for count in range(16):

            for i in range(4):
                bit = (count >> i) & 1
                GPIO.output(led_pins[i], bit)

            print("Binary Count:", format(count, '04b'))
            time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()