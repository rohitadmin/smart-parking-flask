# author Rohit Kumar Kasera, 
# Assam University, silchar, Assam-India,
# year 2019-2021

import RPi.GPIO as GPIO
from picamera import PiCamera
import time
import csv
import os
import urllib.request

csvfile = "ultra_distance_plot.csv"
csvfile_2="ultra_distance_plot_2.csv"
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

servo = 14
GPIO_TRIGGER1 = 24
GPIO_ECHO1 = 16


#set GPIO Pins


key= '5UI6JYALG5QPNVG7'
url= 'https://api.thingspeak.com/update?api_key=%s' %key

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
p=GPIO.PWM(servo,50)
p.start(2.5)

def distance(GPIO_TRIGGER,GPIO_ECHO):
    
    GPIO.output(GPIO_TRIGGER, True)

    
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
   
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    
    Total_Time_Spend = StopTime - StartTime
    print ("Time Elapsed:",Total_Time_Spend)
    print ("Start Time:",StartTime)
    print ("Stop Time:",StopTime)
    
    distance = (Total_Time_Spend * 38300) / 2
    print ("Distance:",distance)
    measure_analysis = [StartTime,StopTime,Total_Time_Spend,distance]
    Actual_Distance= round(distance)
    print ("Actual Distance:",Actual_Distance)
    with open(csvfile_2, "a") as output_1:
        writer = csv.writer(output_1, delimiter=",", lineterminator = '\n')
        writer.writerow(measure_analysis)
    return Actual_Distance



if __name__ == '__main__':
    try:
        while True:
            
            dist_measured = distance(GPIO_TRIGGER1,GPIO_ECHO1)
            timeD = time.strftime("%I")+':'+time.strftime("%M")+':'+time.strftime("%S")
            distance_plot= [dist_measured,timeD]
            state1 = 0
            #camera = PiCamera()
            # 50hz frequency

            if dist_measured < 10:
              print ("Vehicle Detected at Distance barriar gate open:",dist_measured, "Time Taken",timeD)
              #camera.start_preview()
              #time.sleep(3)
              #camera.capture('/home/pi/smartparking/vehicle_image/image.jpg')
              p.ChangeDutyCycle(5)
              time.sleep(2)
              p.ChangeDutyCycle(1.5)
              time.sleep(1)
              final_url= url+"&field1=%s" %(dist_measured)
              s= urllib.request.urlopen(final_url)
              #camera.stop_preview()
            else :
              p.ChangeDutyCycle(5)
              time.sleep(1)
              print ("Slot Entering close",dist_measured, "Time Taken",timeD)
              final_url= url+"&field2=%s" %(dist_measured)
              s= urllib.request.urlopen(final_url)

            print("--------------------------------------------------------------------------")
            
            s.close()
            # with open(csvfile, "a") as output:
            #     writer = csv.writer(output, delimiter=",", lineterminator = '\n')
            #     writer.writerow(distance_plot)
            time.sleep(0.1)
            
        
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()





    
    
    # 
    # time.sleep(1)
