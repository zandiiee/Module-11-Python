option = ""

while option != "5":

    print("STUDENT RESULTS MANAGEMENT SYSTEM")
    print("1. Capture student information")
    print("2. Display student results")
    print("3. Save results to file")
    print("4. Read results from file")
    print("5. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        myfile = open("myfile.txt", 'w')
        myfile.write("Student Information\n")
        studentName = input("Enter Student Name: ")
        studentID = input("Enter Student ID: ")
        studentAge = input("Enter Student Age: ")
        studentCourse = input("Enter Student Course: ")
        myfile.write(f"Name: {studentName} \nID: {studentID} \nAge: {studentAge} \nCourse: {studentCourse}" )
        myfile.close()

    elif option == "2":
        myfile = open("myfile.txt" , "r+")
        print(myfile.read(100))
        myfile.close()

    elif option == "3":
        myfile = open("myfile.txt", "a")
        myfile.write(input("Enter your results: "))
        myfile.close()

    elif option == "4":
        myfile = open("myfile.txt", "r")
        print(myfile.read())
        myfile.close()

    elif option == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try Again")