# author Rohit Kumar Kasera, 
# Assam University, silchar, Assam-India,
# year 2019-2021

from flask import Flask, render_template, request
from flask_mail import Mail, Message
import sqlite3 as sql

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'fd'
app.config['MAIL_PASSWORD'] = 'cd'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

Database_name= 'smart_parking_system.db'

def get_slot_data():
    con = sql.connect(Database_name)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT  slot_name, floor_name, slot_status, vehicle_license_number FROM  parking_slot INNER JOIN parking_floor ON parking_floor.ID = parking_slot.park_floor INNER JOIN user_parking ON user_parking.ID = parking_slot.user_park_id")
    rows =cur.fetchall();
    con.close()
    return rows


def get_park_user():
    con = sql.connect(Database_name)
    con.row_factory = sql.Row
    cur = con.cursor()
    
    cur.execute("SELECT  name,  vehicle_name,  vehicle_type, vehicle_model, vehicle_license_number FROM  user_parking INNER JOIN vehicle_register ON vehicle_register.ID = user_parking.vehicle_name_id INNER JOIN vehicle_size ON vehicle_size.ID= vehicle_register.vehicle_id")
    parkingUser = cur.fetchall();
    con.close()
    return parkingUser

def get_fourvehicle_list():
    con = sql.connect(Database_name)
    con.row_factory = sql.Row
    cur = con.cursor()
    
    cur.execute("SELECT  vehicle_name, vehicle_type FROM vehicle_size WHERE vehicle_type = 'Fourwheeler'")
    fourvehicle_list = cur.fetchall();
    con.close()
    return fourvehicle_list

def get_twovehicle_list():
    con = sql.connect(Database_name)
    con.row_factory = sql.Row
    cur = con.cursor()
    
    cur.execute("SELECT  vehicle_name,  vehicle_type FROM  vehicle_size WHERE vehicle_type = 'Twowheeler'")
    twovehicle_list = cur.fetchall();
    con.close()
    return twovehicle_list


@app.route("/", methods=['GET', 'POST'])
@app.route("/index")
def index_page():
    con = sql.connect(Database_name)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT  slot_number, sensor_status, license_number FROM  Ir_sensor_data WHERE slot_number = 1")
    slotquerydata =cur.fetchall();
    slot_number = []
    sensor_status = []
    license_number =[]
    for listitem in slotquerydata:
        slot_number.append(listitem[0])
        sensor_status.append(listitem[1])
        license_number.append(listitem[2])
    bar_slot_number = slot_number
    bar_sensor_status = sensor_status
    bar_license_number = license_number
    saved_fourvehicletype_list= get_fourvehicle_list()
    saved_twovehicletype_list= get_twovehicle_list()
    msg = Message('Congratualation', sender = 'jadu4k9@gmail.com', recipients = ['developertech2017@outlook.com'])
    msg.body = "parking slot allocated. Slot number : 1  Vehicle License Number: UP3456, Floor Number: 2s"
    mail.send(msg)
    return render_template("index.html",bar_slot_number=bar_slot_number, bar_sensor_status=bar_sensor_status, bar_license_number= bar_license_number, saved_fourvehicletype_list=saved_fourvehicletype_list, saved_twovehicletype_list=saved_twovehicletype_list)

@app.route("/table")
def table_page():
    slotData=get_slot_data()
    parkuser_data = get_park_user()
    return render_template("/table.html" ,slotData = slotData, parkuser_data = parkuser_data)


@app.route("/chart")
def chart_page():
   return render_template("/chart.html")

@app.route("/map")
def map_page():
   return render_template("/map.html")


app.run(debug=True)