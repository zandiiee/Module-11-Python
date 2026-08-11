"""""
Program Name: Student Results Management System
Developer: Leigh-Rae
Date: 11 August 2026
Purpose: Demonstrate exception handling in Python.
"""

def get_mark():
    """
    Gets a student's mark and handles invalid input.
    """
    try:
        # Ask the user to enter a mark
        mark = float(input("Enter the student's mark: "))

        # Check that the mark is within the valid range
        if mark < 0 or mark > 100:
            raise ValueError("Mark must be between 0 and 100.")

        return mark

    except ValueError as error:
        # Handle invalid numbers or marks outside the valid range
        print("Invalid input:", error)
        return None

    finally:
        # This code runs whether an error occurs or not
        print("Input processing completed.")


# Call the function
student_mark = get_mark()

if student_mark is not None:
    print("Student mark:", student_mark)
