age = int(input("Enter the age"))
if age<16:
    print("Price is £3")
elif age>=60:
    print("Price is £2")
else:
    print("Price is £6")


num1 =int(input("Enter the first number: "))
num2 =int(input("Enter the second number: "))
num3 =int(input("Enter the third number: "))
greatest = max(num1, num2, num3)
print(f"The greatest number is: {greatest}")

num = int(input("Enter a number: "))
fact =1
for i in range(1,num+ 1):
    fact*= i
print(f"The factorial of {num} is: {fact}")


num5 =int(input("Enter a number"))
reverse_num=0
while num5 > 0:
    reverse_num = reverse_num * 10 + num5% 10
    num5 //= 10
print(f"The reversed number is: {reverse_num}")


num7 =int(input("Enter a number: "))
limit = int(input("Enter the limit: "))
print(f"Multiples of {num7} up to {limit}:")
for l in range(1, limit + 1):
    if l % num7 == 0:
        print(l)


while True:
    user_input = input()
    if user_input == "done":
        print("Done")
        break
    else:
        print(user_input)


for f in range(1, 11):
    if f % 3 == 0 and f % 5 == 0:
        print("FizzBuzz")
    elif f % 3 == 0:
        print("Fizz")
    elif f % 5 == 0:
        print("Buzz")
    else:
        print(f)


for k in range(5, 0, -1):
    for j in range(k, 0, -1):
        print(j, end=" ")
    print()





