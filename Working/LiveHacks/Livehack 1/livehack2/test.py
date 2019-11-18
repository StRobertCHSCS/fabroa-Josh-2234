'''
-------------------------------------------------------------------------------
Name:		Test.py
Purpose:	triangle checker

Author:	Branaza J

Created:	date in 18/11/2019
------------------------------------------------------------------------------
'''
#welcome to triangle checker
#please enter your angles
angle1 = float(input("please enter the first angle: "))
angle2 = float(input("please enter the seond angle: "))
angle3 = float(input("please enter the third angle: "))



#compute and show what type of triangle it is
if angle1 == 60 and angle2 == 60 and angle3 == 60:
    print("equilateral")

elif angle1 + angle2 + angle3 == 180:
    print("isosceles")

elif angle1 == angle2 and angle1 + angle2 + angle3 == 180:
    print("scalene")

else:
    print("error")