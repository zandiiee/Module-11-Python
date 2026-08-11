"""
Program Name: Student Results Management System
Developer: Zandile Zulu
Date: 11 August 2026
Purpose: Capture, calculate, display and save student results.
"""


# Function to calculate the total of the student's marks
def calculate_total(marks):
    """
    Calculates and returns the total of all student marks.

    Parameters:
        marks: A list containing the student's subject marks.

    Output:
        The total of all marks.
    """
    total = sum(marks)
    return total


# Function to calculate the student's average
def calculate_average(total, number_of_subjects):
    """
    Calculates and returns the average student mark.

    Parameters:
        total: The total of all subject marks.
        number_of_subjects: The number of subjects.

    Output:
        The calculated average mark.
    """
    average = total / number_of_subjects
    return average


# Function to determine whether the student passed or failed
def check_result(average):
    """
    Determines whether the student has passed or failed.

    Parameters:
        average: The student's average mark.

    Outout:
        "Pass" if the average is 50 or higher, otherwise "Fail".
    """
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


# Function to display the student's results
def display_results(name, total, average, result):
    """
    Displays the student's name, total, average and final result.

    Parameters:
        name: The student's name.
        total: The total of all marks.
        average: The student's average mark.
        result: The student's pass or fail result.

    Output:
        None.
    """
    print("\n--- Student Results ---")
    print("Name:", name)
    print("Total:", total)
    print("Average:", average)  # Display the calculated average
    print("Result:", result)


# Get the student's information
student_name = input("Enter student name: ")

# Store the marks for each subject
marks = [70, 65, 80, 55]

# Calculate the student's total and average
total_marks = calculate_total(marks)
average_mark = calculate_average(total_marks, len(marks))

# Check if the student passed or failed
final_result = check_result(average_mark)

# Display the final results
display_results(student_name, total_marks, average_mark, final_result)
