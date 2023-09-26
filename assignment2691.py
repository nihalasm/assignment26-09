
try:
    hourly_rate = float(input("Enter rate: ")) 
    working_hours = int(input("Enter total hours: "))

    if working_hours > 40:
        total_salary = (40 * hourly_rate) + ((working_hours - 40) * 1.5 * hourly_rate)
    else:
        total_salary = working_hours * hourly_rate

    print("total_salary:", total_salary)

except ValueError:
    print("Enter a proper value")