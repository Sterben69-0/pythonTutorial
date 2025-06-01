str = "i am a string"
print(str.endswith("ing"))  # Check if the string ends with "ing"
print(str.startswith("i am"))  # Check if the string starts with "i am"
print(str.find("a"))  # Find the first occurrence of "a"
print(str.isalnum())  # Check if the string is alphanumeric
print(str.capitalize())  # Capitalize the first letter of the string
print(str.replace("a", "o"))  # Replace "a" with "o"
print(str.count("a"))  # Count the number of occurrences of "a"

# # //! Practice
# name = input("What is your name?")
# print("length of name:", len(name))

sal = int(input("What is your Salary?"))
if sal == 50000:
    print("tax=", sal * 0.1)
elif sal > 50000:
    print("tax=", sal * 0.2)
else:
    print("You are poor")
