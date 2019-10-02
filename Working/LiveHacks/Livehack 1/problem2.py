'''
-------------------------------------------------------------------------------
Name:		avg_chicken.py
Purpose:	Determine the amount of chicken each person gets 

Author:	Braganza.J

Created:	date in 02/10/2019 
------------------------------------------------------------------------------
'''
# get the number of people
people = int(input("enter the amount of people"))  

# get the number of chicken
chicken = float(input("enter the amount of pieces of Popeyes chicken"))

# find the class food
Class_food = people/chicken 

#output statement 
print("each person will get ", Class_food, "chicken")

# find mr fabroa chicken 
print ("everything after the decimal place in", Class_food, "is Mr. Fabroa's chicken")