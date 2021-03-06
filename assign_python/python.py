# import relevent pakages 
import datetime
import re
import csv


# Accept date input from user
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

# Accept time input from user
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
            
            start_datetime = datetime.datetime.combine(date1, time1)

# Generate current system date and time
import datetime
current_datetime = datetime.datetime.now()
hsot = current_datetime - start_datetime

# Convert days to hours and multiple by the dollar value
sdays = hsot.seconds//3600
mdays = (hsot.days) * 24

totalhr = sdays + mdays
wage = totalhr * 5

print('Nana, you have worked: {}'.format (hsot))
print('Nana, you have made a total wage of: {} dollas'.format(wage))


##### Save the input and output from the program into a csv file.

# field names  
fields = ['Date_Time of project start','Hours Worked', 'Total Wages']  
    
# data rows of csv file  
rows = [ [start_datetime,hsot, wage ]]  
    
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


