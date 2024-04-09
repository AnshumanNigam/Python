x=5

def my_func():
    y=10
    global x
    x=6
    print(y)
    print(x)

my_func()
print(x)
