# Using conditional operator
# ? Using if, elif and else statement

sal = int(input("What is your Salary?"))
if sal == 50000:
    print("tax=", sal * 0.1)
elif sal > 50000:
    print("tax=", sal * 0.2)
else:
    print("You are poor")

# #! Nesting

age = int(input("How old are you?"))

if age >= 18:
    if age >= 80:
        print("You are too old to drive")
    else:
        print("Can drive")
else:
    print("Too young to drive")

# * Using conditional operator and logical operator

num1 = int(input("enter a number"))
num2 = int(input("enter one more"))
num3 = int(input("one last"))
num4 = int(input("ok this is the last one"))
if num1 > num2 and num1 > num3 and num1 > num4:
    print(num1)
elif num2 > num3 and num2 > num4:
    print(num2)
elif num3 > num4:
    print(num3)
else:
    print(num4)
