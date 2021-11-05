# author Rohit Kumar Kasera, 
# Assam University, silchar, Assam-India,
# year 2019-2021

import RPi.GPIO as GPIO
import time
import csv
import os
import urllib.request


pir_motion = 17
servo = 14

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_motion, GPIO.IN)

GPIO.setup(servo, GPIO.OUT)
p=GPIO.PWM(servo,50)
p.start(2.5)


try:
    while True:
        if GPIO.input(pir_motion):
            print("Human Deducted! slot gate open")
            time.sleep(2)
            p.ChangeDutyCycle(5)
            time.sleep(2)
            p.ChangeDutyCycle(1.5)
            time.sleep(1)
                    
                    #final_url= url+"&field2=%s" %(wrong_slot)
                    #s= urllib.request.urlopen(final_url)
        else:
            print ("Human not detected")
            time.sleep(1)
            p.ChangeDutyCycle(5)
            time.sleep(1)
        #print ("Slot Entering close",dist_measured, "Time Taken",timeD)
        

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()