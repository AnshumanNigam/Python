#for loop

# name="Abhishek"
# for i in name:
#       print(i,end=",")

# colors=["Red","Blue","Green","Purple"]
# for x in colors:
#      print(x)

# #  range()

# for i in range(5):
#       print(i)

# for k in range(9,15):
#      print(k)

# for i in range(10,2,-2):
#     print(i)

# While loop

# count=5
# while(count>0):
#     print(count)
#     count=count-1

# Else with While Loop

# x=5
# while(x>0):
#     print(x)
#     x=x-1
# else:
#     print("counter is 0")

# Do-While loop

# while True:
#     number=int(input("Enter a positive number: "))
#     print(number)
#     if not number>=0:
#         break

# Break statement

# for i in range(1,101,1):
#     print(i,end=" ")
#     if(i==50):
#         break
#     else:
#         print("Mississipi")
# print("Thankyou!!")

# Continue Statement

for i in [2,3,4,6,8,0]:
    if(i%2!=0):
        continue
    print(i)