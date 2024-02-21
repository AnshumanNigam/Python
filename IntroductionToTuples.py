# Similar to lists but tuple are immutable and () is necessary to define tuple
tup=(1,5,6)
print(type(tup),tup)

# Supports multiple data types
tup=(1,2,7,6,"green",True)
print(type(tup),tup)
print(tup[0])
print(tup[4])

# If we just input one element and use a comma then the datatype would be of that element.
# To remain it as a tuple then it needs to be separated by a comma

met=(1)
print(type(met),met)
met=(1,)
print(type(met),met)

examp=(2,45,6,89)
if 89 in examp:
    print("Yes 89 is present in the tuple")
else:
    print("89 is not present in the tuple")