lst1=[1,2,3,4,2,5,6]
lst2=["Red","Green","Blue"]
details=["Abhijeet",18,"FYBscIT",9.8]

print(lst1)
print(lst2)
print(details)

colors=["Red","Green","Blue","Yellow","Pink"]
print(colors[2])
print(colors[0])
print(colors[3])

print(colors[-1])
print(colors[-4])

if "Yellow" in colors:
    print("Yellow is present")
else:
    print("Yellow is absent")

if "maroon" in colors:
    print("Maroon is present")
else:
    print("Maroon is absent")

animals=["cat","dog","bat","mouse","pig","buffaloe"]
print(animals[1:4])
print(animals[-3:-1])
print(animals[1:5:2])

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])

# List Comprehension

names=["Milo","Sarah","Bruno","Anatasia","Rosa"]
namesWith_o=[item for item in names if "o" in item]
print(namesWith_o)

names=["Milo","Sarah","Bruno","Anatasia","Rosa"]
names_o=[item for item in names if (len(item)>4)]
print(names_o)