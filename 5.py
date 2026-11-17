#  DHT11 data upload to ThingSpeak

import http.client
import urllib.parse
import time
import board
import adafruit_dht
import psutil

key = "KEY"  # Put your API Key here

# Kill existing libgpiod process
for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()

sensor = adafruit_dht.DHT11(board.D4)

def thermometer():
    while True:
        try:
            temp = sensor.temperature
            humidity = sensor.humidity

            params = urllib.parse.urlencode({
                'field1': temp,
                'field2': humidity,
                'key': key
            })

            headers = {
                "Content-type": "application/x-www-form-urlencoded",
                "Accept": "text/plain"
            }

            conn = http.client.HTTPConnection("api.thingspeak.com:80")

            conn.request("POST", "/update", params, headers)

            response = conn.getresponse()

            print("Temperature: {}*C Humidity: {}%".format(temp, humidity))
            print(response.status, response.reason)

            data = response.read()
            conn.close()

        except Exception:
            print("connection failed")
            break

        time.sleep(20)


if __name__ == "__main__":
    while True:
        thermometer()