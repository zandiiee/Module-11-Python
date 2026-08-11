programmingMark = 87
databaseMark = 90
webDevelopmentMark = 95

totalMarks = programmingMark + databaseMark + webDevelopmentMark
print(totalMarks)

marks = [87 , 90 , 95]
average = sum(marks) / len(marks)
print(average)

print(max(marks))
print(min(marks))

if average >= 50:
    print('The average is greater then 50')

if programmingMark >= 40:
    print('Programming Mark is greater than 40')
else:
    print('Programming Mark is not greater than 40')

if databaseMark >= 40:
    print('Database Mark is greater than 40')
else:
    print('Database Mark is not greater than 40')

if webDevelopmentMark >= 40:
    print('Web Development Mark is greater than 40')
else:
    print('Web Development Mark is not greater than 40')



if programmingMark <= 75:
    print('Programming Mark is greater than 75')
else:
    print('Programming Mark is not greater than 75')

if databaseMark <= 75:
    print('Database Mark is greater than 75')
else:
    print('Database Mark is not greater than 75')

if webDevelopmentMark <= 75:
    print('Web Development Mark is greater than 75')
else:
    print('Web Development Mark is not greater than 75')


registrationFee = 200
if registrationFee >= 200:
    print('Registration Fee is greater than  and equals to 200')
else:
    print('Registration Fee is not greater than or equal to 200')