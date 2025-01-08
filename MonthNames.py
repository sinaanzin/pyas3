month = int(input("Enter the number"))
months = [ "January", "February", "March", "April", "May", "June","July", "August", "September", "October",
           "November", "December"]
if 1 <= month <= 12:
    print(f"Month {month} is {months[month - 1]}")
else:
    print("Invalid month number!")

age = int(input("Enter the age"))
if age<16:
    print("Price is £3")
elif age>=60:
    print("Price is £2")
else:
    print("Price is £6")

