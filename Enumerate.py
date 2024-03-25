# Enumerate
fruits=["apple","banana","mango"]
for index,fruit in enumerate(fruits):
    print(index,fruit)

print("     ")
# We can change the start index

animal=["mouse","fox","elephant","eagle"]
for index,c in enumerate(animal,start=1):
    print(index,c)
 

print("    ")
# Enumeration in Tuple

colors=("red","yellow","blue","green")
for index,color in enumerate(colors,start=1):
    print(index,color)

print("     ")

# Enumeration in Strings

# s="Hello My name is Anshuman"
# for index,ss in enumerate(s,start=1):
#     print(index,ss)

print("    ")

marks = [12, 56, 32, 98, 12,  45, 1, 4]
for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):         
          print("Harry, awesome!")