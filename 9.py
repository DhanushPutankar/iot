#  IR sensor data with timestamps in MySQL database

import time
import datetime
import csv
import MySQLdb
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.cleanup()

pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

db = MySQLdb.connect(
    host="localhost",
    user="exampleuser",
    passwd="pimylifeup",
    db="exampledb"
)

cur = db.cursor()

while True:

    # Collect sensor data
    degrees = GPIO.input(pin)

    timenow = datetime.datetime.utcnow()

    print(degrees)

    # Insert data into MySQL database
    cur.execute(''' INSERT INTO Sensorstats(date_time, irsensorstat) VALUES(%s,%s); ''', (timenow, degrees))

    db.commit()

    # Wait for 1 second
    time.sleep(1)