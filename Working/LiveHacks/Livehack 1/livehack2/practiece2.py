#get marks, earnings
marks = float(input("please enter the avreage: "))
earnings = float(input("please enter the money you earned: "))


#compute and show destinations
if marks >= 80 and earnings >= 500: 
    print("you get to go to Europe")
elif marks >= 80:
    print("you get to go to california")
else:
    print("your staying home like a good doggo")