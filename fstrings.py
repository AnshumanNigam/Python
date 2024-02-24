name="Alice"
age=30
print(f"My name is {name} and age is {age}")

def greet(name):
    print(f"Hello my name is {name}")
greet(input("Enter your name: "))

# Write a Python program that takes user input for their name and birth year 
# and then prints a formatted message using an f-string to display their name and age.
# Demo Code:=
# Enter your name: Alice
# Enter your birth year: 1990
# Hello, Alice! You are 32 years old.

name=str(input("Enter your Name: "))
year=int(input("Enter your Birth Year: "))
print(f"Hello, {name}! You are {2024-year} years old")

# Write a Python program that takes user input for the length and width of a rectangle and calculates its area and perimeter. 
# Then, print a formatted message using f-strings to display the calculated area and perimeter.
# Demo Code:=
# Enter the length of the rectangle: 5
# Enter the width of the rectangle: 3
# The area of the rectangle is 15 square units, and the perimeter is 16 units.

length=int(input("Enter length of the rectangle: "))
width=int(input("Enter width of the rectangle: "))

if(length<=0 or width<=0):
    print("Error cannot calculate please try again")
else:
    print(f"The area of the rectangle is {length*width} square units, and the perimeter is {2*(length+width)}")





