#LED control with delays using Raspberry Pi 

import RPi.GPIO as GPIO
import time

pin = 18

# Setting the GPIO pins referring mode to BCM
GPIO.setmode(GPIO.BCM)

# Setting the GPIO pin 18 to output mode
GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        # Turn ON the LED
        GPIO.output(pin, True)

        # Time delay for 2 seconds
        time.sleep(2)

        # Turn OFF the LED
        GPIO.output(pin, False)

        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
    exit()