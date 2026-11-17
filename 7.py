#  Motor ON/OFF operation – both directions

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

relay1 = 22
relay2 = 23

GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)

try:
    while True:

        # Clockwise rotation
        GPIO.output(relay1, True)
        GPIO.output(relay2, False)

        print("Motor rotating clockwise")
        time.sleep(5)

        # Stop motor before changing direction
        GPIO.output(relay1, False)
        GPIO.output(relay2, False)
        time.sleep(2)

        # Anticlockwise rotation
        GPIO.output(relay1, False)
        GPIO.output(relay2, True)

        print("Motor rotating anticlockwise")
        time.sleep(5)

        # Stop motor
        GPIO.output(relay1, False)
        GPIO.output(relay2, False)
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.output(relay1, False)
    GPIO.output(relay2, False)
    GPIO.cleanup()