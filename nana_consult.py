import datetime
import re
import csv 



valid = False
while not valid:
    try:
        date = input("Enter the date for the project : ") 
        date_format = '%Y-%m-%d'
        date_obj = datetime.datetime.strptime(date, date_format)
        print(date_obj)
        valid = True
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")

s_valid  = False
while not s_valid:
    try:

        stime = input("Enter the time project started : ")
        time_format = "%H:%M:%S"
        sttime = datetime.datetime.strptime(stime, time_format)
        if re.match(r'\d{2}:\d{2}:\d{2}', str(sttime.time())):
            if str(sttime.time()) < '24:01':
                print(sttime)
                s_valid = True
        
    except ValueError:
        print("Incorrect time format, should be H:M:S")

e_valid  = False
while not e_valid:
    try:
        etime = input("Enter the time project ended : ")
        time_format = "%H:%M:%S"
        ettime = datetime.datetime.strptime(etime, time_format)
        if re.match(r'\d{2}:\d{2}:\d{2}', str(ettime.time())):
            if str(ettime.time()) < '24:01' :
                print(ettime)
                e_valid = True
    except ValueError:
        print("Incorrect data format, should be H:M:S")




hsot = ettime - sttime
wage = hsot * 5

print('Nana, you have worked: {}'.format (hsot))
print('Nana, you have made a total wage of: {}'.format(wage))


 
    
# field names  
fields = ['Hours Worked', 'Total Wages']  
    
# data rows of csv file  
rows = [ [hsot, wage ]]  
    
# name of csv file  
filename = "nana_consulting.csv"
    
# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(rows) 
   
