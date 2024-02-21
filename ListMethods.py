l=[1,2,4,4,4,45,60]

print(l)

l.append(7)
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

print(l.index(4))

print(l.count(4))

m=[11,45,1,2,4,6,1,1]
n=[]
print(m)
n=m.copy()
n[0]=0
print(l)

p=[2,45,6767,5673]
p.insert(1,45)
print(p)

a=["red","blue","green"]
b=[900,100,200]
a.extend(b)
print(a)

q=a+b
print(q)

kill=["marie","suzie","Jonathan","Tanmay"]
kill.pop(2)
print(kill)
