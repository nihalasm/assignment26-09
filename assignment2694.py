try:
    number = float(input("Enter a number between 0.0 and 100.0 : "))

    if 0.0 <= number <= 100.0:
        if 90.0 <= number <= 100.0:
            grade = 'A'
        elif 80.0 <= number < 90.0:
            grade = 'B'
        elif 70.0 <= number < 80.0:
            grade = 'C'
        elif 60.0 <= number < 70.0:
            grade = 'D'
        elif 50.0 <= number < 60.0:
            grade = 'E'
        else:
            grade = 'F'

        print("Grade:", grade)
    else:
        print("Error: Number is out of range (0.0-100.0).")
except ValueError:
    print("Error: Invalid input. Please enter a valid number between 0.0 and 100.0 .")