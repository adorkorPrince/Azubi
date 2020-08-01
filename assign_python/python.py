print('Hello World')
print(" Iam Richard")
print('I have seen the commit changes down there')




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
