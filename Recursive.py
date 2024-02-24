def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return(num*factorial(num-1))

# factorial called again
    
num=int(input("Enter number: "))
print("Number: ",num)
print("Factorial: ",factorial(num))

# Checking if a string is palindrome or not
def palindrome(input):
    if len(input)<=1:
        return True
    elif input[0]==input[-1]:
        return palindrome(input[1:-1])
    else:
        return False
    
result = palindrome(str(input("Enter the String: ")))

if result:
    print("String is palindrome")
else:
    print("String is not palindrome")