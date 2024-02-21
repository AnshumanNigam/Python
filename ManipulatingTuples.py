countries=("Spain","Italy","India","England","Germany")
temp=list(countries)
# adding item 
temp.append("Russia")
# removing item
temp.pop(1)
# converting back list to tuple 
countries=tuple(temp)
print(countries)

# Concatenating two tuples without converting them into list

countries1 = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries1 + countries2
print(southEastAsia)

# Tuple methods
tup=(1,5,6,7,8,1,2,1,9,1)
print(tup.count(1))

tup1=(0,1,2,3,2,3,1,3,2)
print(tup1.index(3,2,8))