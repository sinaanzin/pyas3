weight = float(input("Enter your weight (kg)"))
height = float(input("Enter your height (m)"))
bmi = weight / (height ** 2)

if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi < 25:
    status = "Normal"
elif 25 <= bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

print(f"Your BMI is: {bmi:.2f}")
print(f"You are in the {status} range")

num1 = int(input("Enter 3 numbers"))
num2 = int(input())
num3 = int(input())
greatest=max(num1,num2,num3)
print(f"{greatest} is the greatest number among them")

number = int(input("Enter a number:"))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is {factorial}")

num = int(input("Enter a number"))
rev_num=0
while num:
    rev_num = rev_num * 10 + num % 10
    num //= 10
print("Reversed number", rev_num)

num = int(input("Enter a number"))
for i in range(1, 11):
    print(f"{num}*{i}={num * i}")

while True:
    a = input("Enter a value: ")
    if a == 'done' or 'DONE':
        print("Done")
        break
    print(a)

for i in range(1, 11):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


