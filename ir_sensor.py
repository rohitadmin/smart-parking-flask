# author Rohit Kumar Kasera, 
# Assam University, silchar, Assam-India,
# year 2019-2021

import sqlite3
import sys

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style
style.use('fivethirtyeight')

import urllib.request
import RPi.GPIO as GPIO
import time

key='456KO7XZNYQBVPXO'
url = 'https://api.thingspeak.com/update?api_key=%s' %key


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(14,GPIO.IN)

Database_name= '/home/pi/project/flasksmartparking/smart_parking_system.db'


def getIRdata():
    GPIO.setup(14,GPIO.IN)
    state=GPIO.input(14)
    if(state==True):
        slot_status='avaible'
        slot_data=1
        sensor_data(slot_status)
        final_url=url+"&field4=%s" %(slot_data)
        s=urllib.request.urlopen(final_url)
    if(state==False):
        slot_status='Parked'
        slot_data = 0
        sensor_data(slot_status)
        final_url=url+"&field4=%s" %(slot_data)
        s=urllib.request.urlopen(final_url)

def sensor_data(slot_status):
    conn = sqlite3.connect(Database_name)
    curs=conn.cursor()
    date= (time.strftime("%Y-%m-%d ") + time.strftime("%H:%M:%S"))
    curs.execute('''INSERT INTO Ir_sensor_data(sensor_status,date_time) VALUES (?,?) ''',(slot_status,date))
    conn.commit()
    conn.close()

def displayData():
    conn=sqlite3.connect(Database_name)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM Ir_sensor_data"):
        print (row)
    conn.close()


def main():
    while(1):
        getIRdata()
        time.sleep(2)
        displayData()


# Execute program 
main()
