'''
-------------------------------------------------------------------------------
Name:		Heating Days Tracker
Purpose:	Determine the heat days 

Author:	Braganza.J

Created:	date in 09/12/2019 
------------------------------------------------------------------------------
'''
#Get the Heat days
Heat_days =int(input("Enter the number of heat days to track: "))

#for loop
for i in range(0,15,Heat_days):
    print(i)
    if i <=15: 
        print("heat day")