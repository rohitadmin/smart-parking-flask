# author Rohit Kumar Kasera, 
# Assam University, silchar, Assam-India,
# year 2019-2021

import time
import sqlite3 as sql

Database_name= 'smart_parking_system.db'

def get_slot_data():
    con = sql.connect(Database_name)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT  slot_name, floor_name, slot_status, slot_type FROM  parking_slot INNER JOIN parking_floor ON parking_floor.ID = parking_slot.park_floor")
    rows =cur.fetchall();
    #final_result_slot = [list(i) for i in rows]
    con.close()
    return rows


def get_park_user():
    con = sql.connect(Database_name)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT  name,  vehicle_name,  vehicle_type, vehicle_model, vehicle_license_number FROM  user_parking INNER JOIN vehicle_register ON vehicle_register.ID = user_parking.vehicle_name_id INNER JOIN vehicle_size ON vehicle_size.ID= vehicle_register.vehicle_id WHERE user_parking.ID=1")
    parkingUser = cur.fetchall();
    #final_result_vehicle = [list(i) for i in parkingUser]
    con.close()
    return parkingUser

recognize_license_plate_list_temp= "UP65BS1433"
vehicle_type_four = "Fourwheeler"
vehicle_type_two= "Twowheeler"
vehicle_type_heavy = "Bus"
temp_slot_status=[]
fun_slot_val=get_slot_data()
fun_park_user=get_park_user()

for row in fun_park_user:
    if recognize_license_plate_list_temp in row[4] and vehicle_type_four in row[2]:
        for slot_row in fun_slot_val:
            if vehicle_type_four in slot_row[3] and slot_row[2]=="Available":
                print(slot_row[2])
    if  recognize_license_plate_list_temp in row[4] and vehicle_type_two in row[2]:
        for slot_row in fun_slot_val:
            if vehicle_type_two in slot_row[3] and slot_row[2]=="Available":
                print(slot_row[2])
            else:
                print("No space available for two wheeler")
    if  recognize_license_plate_list_temp in row[4] and vehicle_type_heavy in row[2]:
        for slot_row in fun_slot_val:
            if vehicle_type_heavy in slot_row[3] and slot_row[2]=="Available":
                print(slot_row[2])
            else:
                print("No space available for heavy vehicle")
    else:
        print("Regonised License plate not matched with registred license plate")

# def get_fourvehicle_list():
#     con = sql.connect(Database_name)
#     con.row_factory = sql.Row
#     cur = con.cursor()
#     cur.execute("SELECT  vehicle_name, vehicle_type FROM vehicle_size WHERE vehicle_type = 'Four Wheeler'")
#     fourvehicle_list = cur.fetchall();
#     con.close()
#     return fourvehicle_list

# def get_twovehicle_list():
#     con = sql.connect(Database_name)
#     con.row_factory = sql.Row
#     cur = con.cursor()
#     cur.execute("SELECT  vehicle_name,  vehicle_type FROM  vehicle_size WHERE vehicle_type = 'Two Wheeler'")
#     twovehicle_list = cur.fetchall();
#     con.close()
#     return twovehicle_list


