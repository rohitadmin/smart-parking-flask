# author Rohit Kumar Kasera, 
# Assam University, silchar, Assam-India,
# year 2019-2021

import dbconnection
import sqlite3

conn = sqlite3.connect(dbconnection)

conn.execute('''CREATE TABLE user_parking
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         mobileno       INT     NOT NULL,
         emailid		TEXT    NOT NULL,
         owneridproof	TEXT    NOT NULL,
         vehicle_id	    INT     NOT NULL,
         ADDRESS        CHAR(50),
         FOREIGN KEY (vehicle_id) REFERENCES vehicle_register (id));''')
print ("Table created successfully")


conn.execute('''CREATE TABLE vehicle_register
         (ID INT PRIMARY KEY     NOT NULL,
         vehicle_name   TEXT    NOT NULL,
         vehicle_license_number TEXT     NOT NULL,
         vehicle_insurance_no      TEXT     NOT NULL,
         vehicle_year		INT    NOT NULL,
         vehicle_type	TEXT    NOT NULL,
         vehicle_registered_state	    TEXT     NOT NULL,
         );''')
print ("Table created successfully")

conn.close()

