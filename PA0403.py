

def login():
     username = input("Enter username: ")
     password = input("Enter password: ")

     if username == "admin" and password == "1234": 
        print("Login successful!\n") 
        return True 
     else: 
        print("Invalid username or password.\n") 
        return False

def capture_student():
    student = {}

    student["full name"] = input("Enter your  full name:")
    student["programming"] = float(input("Enter your Pragramming Mark:"))
    student["database"] = float(input("Enter your Database Mark:"))
    student["webdev"] = float(input("Enter your Web dev Mark:"))

    return student

def calculate_results(student):
    total = (
        student["programming"]
        + student["database"]
        + student["webdev"]
    )

    average = total / 3

    student["total"] = total
    student["average"] = average

    return student

def display_results(student):
    print("\n----- STUDENT RESULTS -----")
    print(f"Name: {student['full name']} \n")
    print(f"Programming: {student['programming']}\n")
    print(f"Database: {student['database']}\n")
    print(f"Web Development: {student['webdev']}\n")
    print(f"Total: {student['total']}\n")
    print(f"Average: {student['average']:.2f}\n")

def save_results(student):
    with open("student_results.txt", "w") as file:
        file.write(f"Name: {student['full name']} \n")
        file.write(f"Programming: {student['programming']}")
        file.write(f"Database: {student['database']}\n")
        file.write(f"Web Development: {student['webdev']}\n")
        file.write(f"Total: {student['total']}\n")
        file.write(f"Average: {student['average']:.2f}\n")

    print("Results saved ")

def read_results():
    try:
     with open("student_results.txt", "r") as file:
        print("\n ------SAVED RESULTS -------")
        print(file.read())
    except FileNotFoundError:
        print("No saved results found")

def display_menu():
    print("\n ----- STUDENT MANAGEMENT SYSTEM ------ ")
    print("1. Capture student information")
    print("2. Display student results")
    print("3. Save results to file")
    print("4. Read results from file")
    print("5. Exit")

def main():
    student = None

    if login():
        while True:  # 1. Added loop here so 'break' works
            display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                student = capture_student()
                student = calculate_results(student)  # 2. Passed student argument
                print("Student info captured")

            elif choice == "2":
                if student:
                    display_results(student)  # 3. Fixed wrong function call
                else:
                    print("Please capture student info first")

            elif choice == "3":
                if student:
                    save_results(student)
                else:
                    print("Please capture student info first")

            elif choice == "4":
                read_results()

            elif choice == "5":
                print("Exiting...")
                break  # This now successfully breaks the while loop!

            else:
                print("Invalid option")

main()
        