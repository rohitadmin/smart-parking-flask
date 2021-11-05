# author Rohit Kumar Kasera, 
# Assam University, silchar, Assam-India,
# year 2019-2021

import sqlite3
from operator import itemgetter 
import numpy as np
import pandas as pd
from tabulate import tabulate

connection=sqlite3.connect('./database/smart_parking_system.db')
connection.row_factory = sqlite3.Row
cursor=connection.cursor()
slot_all_list =[]

def parking_slot_list():
	cursor.execute("SELECT slot_name, slot_status FROM parking_slot where slot_status=1")
	slotquerydata =cursor.fetchall();
    slot_name = []
    slot_status = []
    for listitem in slotquerydata:
        slot_name.append(listitem[0])
        slot_status.append(listitem[1])
    plt.plot_date(slot_name,slot_status)
    plt.savefig('slot.png')



# def available_slot():
# 	slot_detail= parking_slot_list()
# 	result = list(map(itemgetter('slot_status'), slot_detail))
# 	result_bool = np.array(result)
# 	final_val = (result_bool > 0).tolist()
# 	# bool_list = [bool(result)]
# 	return final_val
# print("Available Slot Details",available_slot())


connection.close()


