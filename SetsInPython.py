# Sets are immutable i.e cannot be changed once created

info={"Rajesh","Gentics",False,19}
print(type(info),info)

a1={"A","B","C"}
a2={"a","b","c"}
a3=a1.union(a2)
print(a3)
a1.update(a2)
print(a1)

a4={"A","B","C"}
a5={"A","b","c"}
a6=a4.intersection(a5)
print(a6)
a4.intersection_update(a5)
print(a4)

b1=a4.symmetric_difference(a5)
print(b1)
a4.symmetric_difference_update(a5)
print(a4)

a11={"A","B","d"}
a12={"A","C"}
b21=a11.difference(a12)
print(b21)
a11.difference_update(a12)
print(a11)
print(a11.isdisjoint(a12))

new1={"JEE","NEET","2024","2025"}
new2={"JEE","NEET","doctor","LAW"}

new1.remove("2024")
new2.discard("LAW")
print(new1)
print(new2)

new1.pop()
print(new1)

del new1


new2.clear()
print(new2)