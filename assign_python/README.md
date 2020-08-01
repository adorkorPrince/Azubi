This python application computes the wages paid to a consultant based on the number of hours and minutes he works on client projects. The application accepts as an 
the date and time work was started on the project, it then uses the current systems date and time to compute the wages due the consultant. 
Inputs and outputs to the program are then stored to csv file for future referencing.

------Process Breakdown-------

Users are asked to key-in th date the project started and repeatedly prompted to key in the date in the format YYYY-MM-DD, if not keyed in right.

Then the user is asked to key-in the time the project started in the format H:M:S, and repeatedly prompted if the format is wrong.

The time and date are then combined and subtracting the current systen time to get total hours worked.

The days worked are connected to hours and multipled with $5 to arrive at the total wages made on the project
