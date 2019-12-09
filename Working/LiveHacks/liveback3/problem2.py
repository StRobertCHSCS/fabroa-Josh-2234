'''
-------------------------------------------------------------------------------
Name:		Welcome to the Distance Tracker
Purpose:	Determine the amount of times ge had to travel before he got to 100km

Author:	Braganza.J

Created:	date in 09/12/2019 
------------------------------------------------------------------------------
'''
#get distances 
days = int(input("enter the days traveled: "))

# initalize total
total = 0 
#cumpute the distances
for i in range(1,100,days):
    #get distance
    distance_travalled = float(input("enter the distance: "))
    total = total + distance_travalled

#compute average
average = total/days

print("it took " + str(days) + "to surpass 100k driven " +str(average))