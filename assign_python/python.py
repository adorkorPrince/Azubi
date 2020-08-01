import datetime

import re
import csv



valid = False
while not valid:
    try:
        sdate = input("Enter the date for the project : ") 
        date_format = '%Y-%m-%d'
        sdate_obj = datetime.datetime.strptime(sdate, date_format)
        date1 = sdate_obj.date()
        valid = True
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD"))

s_valid  = False
while not s_valid:
    try:

        stime = input("Enter the time project started : ")
        time_format = "%H:%M:%S"
        sttime = datetime.datetime.strptime(stime, time_format)
        if re.match(r'\d{2}:\d{2}:\d{2}', str(sttime.time())):
            if str(sttime.time()) < '24:01':
                time1 = sttime.time()
                s_valid = True
    except ValueError:
            print("Incorrect time format, should be H:M:S")