# Built-in function

print(min([1,3,6,0]))
print(min(["apple","kiwi","bananas"]))
print(max([5,4,89,110]))
print(len(["hello"]))
print(len([1,2,3,4,5]))
print(sum([2,5,1]))
print(sum(range(5)))
print(type(43))
print(range(2,10,2))
print(dict([(1,"a"),(2,"b")]))
print(list("hello"))
print(set("apple"))
print("1,2,3",sep=",")

# User-defined function

def newfunction (fname,lname):
    print("hello, ",fname,lname )

fname=str(input("Enter First name: "))
lname=str(input("Enter Last name: "))
newfunction(fname,lname)

def newfunction(FirstNo,SecondNo):
    print("The sum of the given number is---> ",FirstNo+SecondNo)

FirstNo=int(input("First Number: "))
SecondNo=int(input("Second Number: "))
newfunction(FirstNo,SecondNo)

