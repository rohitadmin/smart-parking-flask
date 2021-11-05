# author Rohit Kumar Kasera, 
# Assam University, silchar, Assam-India,
# year 2019-2021

import RPi.GPIO as GPIO
from picamera import PiCamera
import time
import csv
import os
import urllib.request
import re
import sqlite3 as sql

pir_motion = 17
servo = 14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_motion, GPIO.IN)

Database_name= 'smart_parking_system.db'

def get_vehicle_plate_list():
    con = sql.connect(Database_name)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT  vehicle_license_number FROM  user_parking  INNER JOIN parking_slot ON user_parking.ID = parking_slot.user_park_id WHERE  parking_slot.slot_name= 'marutitwo'")
    list_vehicle = cur.fetchall();
    con.close()
    return list_vehicle

orignal_list_plate = get_vehicle_plate_list()
test_str = "WB02W6886"

key= 'S80MFNR4BLLYF8XJ'
url= 'https://api.thingspeak.com/update?api_key=%s' %key
slot_verified = 1
wrong_slot =0

GPIO.setup(servo, GPIO.OUT)
p=GPIO.PWM(servo,50)
p.start(2.5)
camera = PiCamera()

try:
    while True:
        if GPIO.input(pir_motion):
            print("Vehicle Deducted")
            time.sleep(2)
            camera.start_preview()
            time.sleep(3)
            camera.capture('/home/pi/project/flasksmartparking/vehicle_image/image1.jpg')
            camera.stop_preview()
            for match in orignal_list_plate:
                if test_str in match:
                    print("The allocated slot is verified for License plate",test_str)
                    print("slot gate is open for parking the vehicle")
                    p.ChangeDutyCycle(5)
                    time.sleep(2)
                    p.ChangeDutyCycle(1.5)
                    time.sleep(1)
                    #final_url= url+"&field1=%s" %(slot_verified)
                    #s= urllib.request.urlopen(final_url)
                else:
                    print("Input License plate mot matches for the allocated slot number, Vehicle arrived at wrong slot")
                    p.ChangeDutyCycle(5)
                    time.sleep(1)
                    #final_url= url+"&field2=%s" %(wrong_slot)
                    #s= urllib.request.urlopen(final_url)
        else:
            print ("vehicle not detected")
            time.sleep(1)
        #print ("Slot Entering close",dist_measured, "Time Taken",timeD)
        

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()