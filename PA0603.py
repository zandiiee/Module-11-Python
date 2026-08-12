import os
from datetime import datetime
import math
# os module
if os.path.exists("student_results.txt"):
    print("File exists")
else:
    print("File does not exist")
# current directory
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")
# checking if file exists
if not os.path.exists("student_records"):
    os.mkdir("student_records")

#current time
now = datetime.now()
print(now) 


created_date = str(datetime.now())

with open("result.txt", "w") as file:
    file.write(f"Created On: {created_date}\n")

print(created_date)
# string date 
num_date = 20260812
new_date = str(num_date)

months = ["", "January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

year = new_date[:4]
month = months[int(new_date[4:6])]
day = str(int(new_date[6:]))

print(f"{month} {day}, {year}")

marks = [45, 67, 32, 89, 50, 25]

total = sum(marks)
average = total / len(marks)

print("Total mark:", total)
print("Average mark:", average)

print("Average rounded upwards:", math.ceil(average))

print("Average rounded downwards:", math.floor(average))

print("Square root of total mark:", math.sqrt(total))