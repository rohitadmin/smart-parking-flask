# author Rohit Kumar Kasera, 
# Assam University, silchar, Assam-India,
# year 2019-2021

import sqlite3
import sys

import matplotlib.pyplot as plt
#matplotlib.use('Agg') 
plt.style.use('ggplot')



import time
Database_name= '/home/pi/project/flasksmartparking/smart_parking_system.db'

conn = sqlite3.connect(Database_name)
c = conn.cursor()

c.execute('SELECT sensor_status, date_time  FROM Ir_sensor_slot_data')
data = c.fetchall()
Ir_data = []
datetime = []
    
for row in data:
   # print(row)
    Ir_data.append(row[0])
    datetime.append(row[1])
#conn.close()
plt.plot(datetime,Ir_data)
plt.xlabel('Time and Date')
plt.ylabel('Status')
plt.show()
