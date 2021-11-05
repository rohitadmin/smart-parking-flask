# author Rohit Kumar Kasera, 
# Assam University, silchar, Assam-India,
# year 2019-2021

import sqlite3

connection = sqlite3.connect('./database/smart_parking_system.db')
print("connected successfully")


connection.execute('''CREATE TABLE user_parking
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


connection.execute('''CREATE TABLE vehicle_register
         (ID INT PRIMARY KEY     NOT NULL,
         vehicle_name   TEXT    NOT NULL,
         vehicle_license_number TEXT     NOT NULL,
         vehicle_insurance_no      TEXT     NOT NULL,
         vehicle_year		INT    NOT NULL,
         vehicle_type	TEXT    NOT NULL,
         vehicle_model  INT    NOT NULL,
         vehicle_model_size  INT    NOT NULL,
         vehicle_registered_state	    TEXT     NOT NULL,
         FOREIGN KEY (vehicle_model_size) REFERENCES vehicle_size (id),
         FOREIGN KEY (vehicle_model) REFERENCES vehicle_size (id)
         );''')
print ("Table created successfully")


connection.execute('''CREATE TABLE parking_floor
         (ID INT PRIMARY KEY     NOT NULL,
         floor_name   TEXT    NOT NULL
         );''')
print ("Table created successfully")

connection.execute('''CREATE TABLE floor_wings
         (ID INT PRIMARY KEY     NOT NULL,
         wings_name   TEXT    NOT NULL,
         floor_id     INT     NOT NULL,
         FOREIGN KEY (floor_id) REFERENCES parking_floor (id)
         );''')
print ("Table created successfully")

connection.execute('''CREATE TABLE parking_slot
         (ID INT PRIMARY KEY     NOT NULL,
         slot_name   TEXT    NOT NULL,
         park_floor   INT      NOT NULL,
         slot_size   TEXT      NOT NULL,
         slot_status   BOOLEAN DEFAULT(TRUE),
         park_vehicle  TEXT DEFAULT none,
         FOREIGN KEY (park_floor) REFERENCES parking_floor (id)
         );''')
print ("Table created successfully")

connection.execute('''CREATE TABLE vehicle_size
         (ID INT PRIMARY KEY     NOT NULL,
         vehicle_name   TEXT    NOT NULL,
         vehicle_size   TEXT    NOT NULL,
         vehicle_model   TEXT      NOT NULL
         );''')
print ("Table created successfully")

connection.execute("INSERT INTO parking_slot (ID,slot_name,slot_wings,park_floor) \
      VALUES (1, 'one', 1, 1 )");

connection.commit()
print ("Records created successfully")

connection.execute("INSERT INTO parking_slot (ID,slot_name,slot_wings,park_floor) \
      VALUES (2, '2', 1, 1 )");

connection.commit()
print ("Records created successfully")

connection.execute("INSERT INTO parking_slot (ID,slot_name,slot_wings,park_floor) \
      VALUES (3, '3', 1, 1 )");

connection.commit()
print ("Records created successfully")
connection.execute("INSERT INTO parking_slot (ID,slot_name,slot_wings,park_floor) \
      VALUES (4, '4', 1, 1 )");

connection.commit()
print ("Records created successfully")
connection.execute("INSERT INTO parking_slot (ID,slot_name,slot_wings,park_floor) \
      VALUES (5, '5', 1, 1 )");

connection.commit()
print ("Records created successfully")
connection.execute("INSERT INTO parking_slot (ID,slot_name,slot_wings,park_floor) \
      VALUES (6, '6', 1, 1 )");

connection.commit()
print ("Records created successfully")
connection.execute("INSERT INTO parking_slot (ID,slot_name,slot_wings,park_floor) \
      VALUES (7, '7', 1, 1 )");

connection.commit()
print ("Records created successfully")
connection.execute("INSERT INTO parking_slot (ID,slot_name,slot_wings,park_floor) \
      VALUES (8, '8', 1, 1 )");

connection.commit()
print ("Records created successfully")
connection.execute("INSERT INTO parking_slot (ID,slot_name,slot_wings,park_floor) \
      VALUES (9, '9', 1, 1 )");

connection.commit()
print ("Records created successfully")
connection.execute("INSERT INTO parking_slot (ID,slot_name,slot_wings,park_floor) \
      VALUES (10, '10', 1, 1 )");

connection.commit()
print ("Records created successfully")
connection.execute("INSERT INTO parking_slot (ID,slot_name,slot_wings,park_floor) \
      VALUES (11, '11', 2, 1 )");

connection.commit()
print ("Records created successfully")
connection.execute("INSERT INTO parking_slot (ID,slot_name,slot_wings,park_floor) \
      VALUES (12, '12', 2, 1 )");

connection.commit()
print ("Records created successfully")

connection.execute("INSERT INTO parking_slot (ID,slot_name,slot_wings,park_floor) \
      VALUES (13, '13', 2, 1 )");

connection.commit()
print ("Records created successfully")
connection.close()