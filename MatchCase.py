x=11
match x:
    case 0:
        print("x is zero")
    case 4 if (x%2==0):
        print("x is 4")
    case 3:
        print("x is not a number")
    case _ if(x<10):
        print("Number is less than 10")
    case _:
        print("This is the default case")
