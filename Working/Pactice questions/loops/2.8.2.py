#get number
number = int(input("enter a number: "))

#initalize total
total = 0

#compute the total
for i in range(1,number+1,2):
    #print(i)
    total = total + 1

#output total
print(total)
