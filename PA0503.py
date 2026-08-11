"""
Program Name: Student Results Management System
Developer: Leigh-Rae
Date: 11 August 2026
Purpose: Capture student information, validate marks,
         calculate results and handle common errors.
"""


# Get and validate the student's age
def get_age():
    """
    Gets the student's age and handles invalid input.
    """
    try:
        age = int(input("Enter student's age: "))

        if age <= 0:
            raise ValueError("Age must be greater than 0.")

    except ValueError as error:
        print("Invalid age:", error)
        return None

    else:
        print("Age accepted.")
        return age

    finally:
        print("Age entry process completed.")


# Get and validate the student's mark
def get_mark():
    """
    Gets the student's mark and checks that it is
    between 0 and 100.
    """
    try:
        mark = float(input("Enter student's mark: "))

        if mark < 0 or mark > 100:
            raise ValueError("Mark must be between 0 and 100.")

    except ValueError as error:
        print("Invalid mark:", error)
        return None

    else:
        print("Mark accepted.")
        return mark

    finally:
        print("Mark entry process completed.")


# Calculate the average mark
def calculate_average(total, number_of_subjects):
    """
    Calculates the average mark and handles division by zero.
    """
    try:
        average = total / number_of_subjects

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

    else:
        print("Average calculated successfully.")
        return average

    finally:
        print("Average calculation completed.")


# Read the student's results file
def read_results_file():
    """
    Opens and reads the student's results file.
    Handles a missing file.
    """
    try:
        with open("student_results.txt", "r") as file:
            results = file.read()

    except FileNotFoundError:
        print("Error: The results file could not be found.")
        return None

    else:
        print("Results file opened successfully.")
        return results

    finally:
        print("File reading process completed.")


# ---------------- MAIN PROGRAM ----------------

print("=== Student Results Management System ===")

# Get student information
student_name = input("Enter student's name: ")

student_age = get_age()

student_mark = get_mark()

# Calculate average if a valid mark was entered
if student_mark is not None:
    average = calculate_average(student_mark, 1)

    if average is not None:
        print("Student:", student_name)
        print("Age:", student_age)
        print("Mark:", student_mark)
        print("Average:", average)

# Try to read the results file
print("\nChecking results file...")
read_results_file()
