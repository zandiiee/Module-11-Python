def save_results():
    my_results = open("student_results.txt",'w')
    student_name = input("Enter your full name: ")
    student_number = int(input("Enter your student number: "))
    course_name = input("Enter your course name: ")
    programming_mark = int(input("Enter your programming mark: "))
    database_mark = int(input("Enter your database mark: "))
    webdev_mark = int(input("Enter your web development mark: "))
    total = programming_mark + database_mark + webdev_mark
    avarage = total / 3
    date = "11 August 2026"
    my_results.write(f"Student Name: {student_name}\n Student Number: {student_number}\n Course: {course_name}\n Programming Mark: {programming_mark}\n Database Mark: {database_mark}\n Webdevelopment Mark: {webdev_mark}\n Total: {total}\n Avarage: {avarage}\n Date: {date}")
    my_results.close()

def read_results():
    my_results = open("student_results.txt", "r")
    print(my_results.read())
    my_results.close()

read_results() 