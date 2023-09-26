count = 0
total = 0

while True:
    user_input = input("Enter a value : ")

    if user_input == 'done':
        break

    try:
        number = float(user_input)
        total += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a valid number or 'done'.")

if count > 0:
    average = total / count
    print("Sum:", total)
    print("Count:", count)
    print("Average:", average)
else:
    print("No numbers entered.")