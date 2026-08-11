marks = [65, 72, 80]
total = 0
for mark in marks:
    total += mark
average = total / len(marks)
if average >= 50:
    print("Pass")
else:
    print("Fail")

#1 - The purpose of this list is to display multiple marks within the same varible
#2 - The purpose of the loop is to see which marks are below 50 so that a message can be displayed
#3 - The total is calculated by adding up all of the marks
#4 - The average is calculated dividing the total by the total number of marks
#5 - The final decision is made by comparing the average to 50 to see whether its a pass or fail
#6 -  The expected output is "Pass"