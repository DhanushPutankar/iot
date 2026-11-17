#  Motor ON/OFF operation – one direction using relay


import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

pin1 = 22

GPIO.setup(pin1, GPIO.OUT)

try:
    while True:

        # Motor ON
        GPIO.output(pin1, True)
        time.sleep(5)

        # Motor OFF
        GPIO.output(pin1, False)
        time.sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()

exit()