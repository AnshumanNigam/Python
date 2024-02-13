# This starting program checks if the product you want to buy is in your budget or not. If it is in your budget then it is added in your cart 
# and if not then it is not added and at last your total cart price is given

Budget=int(input("Enter your Budget: "))
print("Items currently available are--> \n 1.Eggs (Rs.6 each) \n 2.Bread(Rs.25) \n 3.Milk packet(Rs.15 each)")
choice=int(input("Enter number what you want to buy: "))
if(choice==1):
    count=int(input("Enter quantity of the product: "))
    total=count*6
elif(choice==2):
    count=int(input("Enter quantity of the product: "))
    total=count*25
elif(choice==3):
    count=int(input("Enter quantity of the product: "))
    total=count*25
else:
    print("wrong choice")
    print(Budget)

if(total<=Budget):
    print("Your total Bill is: ",total,"\n Thank you for shopping")
else:
    print("Your total exceeds your Budget cannot check out please try again later")


