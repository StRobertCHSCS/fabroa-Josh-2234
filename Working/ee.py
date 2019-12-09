# get the number of marks
number_of_marks = int(input("Enter the number of marks: "))

# initialize total
total = 0

# compute the total of the marks
for i in range(number_of_marks):
    # get a mark from the user and add to total
    mark = float(input("Enter a mark: "))
    total = total + mark

# compute average based on total
average = total/number_of_marks

print("The average of the " + str(number_of_marks) + " marks is " +str(average))