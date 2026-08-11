studentNumber = 9845264
studentName = 'Zandile'
studentSurname ='Zulu' 
studentAge = 23 
courseName = 'Criminology' 
fulltimeStudentStatus = 'Full time' 
programmingMark = '87'
databaseMark = '90' 
webDevelopmentMark = '95'  
registrationFee = 200



print( studentName + studentSurname)
print(courseName.upper())
print(len(studentName + studentSurname))

rounded_num = round(registrationFee, 2)
print(rounded_num) 

programmingMark = float(programmingMark)
print(type(programmingMark))

databaseMark = float(databaseMark)
print(type(databaseMark))

webDevelopmentMarkMark = float(webDevelopmentMark)
print(type(webDevelopmentMarkMark))

print(f'Hello, my name is {studentName} {studentSurname} and I am {studentAge} of age')
print( f'I am currently studying {courseName} and my student number is {studentNumber}, I am a {fulltimeStudentStatus} student.')
print(f'My current marks are {programmingMark},{webDevelopmentMark},{databaseMark} for programming, web Development and database respectfully.')
