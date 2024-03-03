info={'name':'Karan','age':19,'eligible':True}
print(type(info),info)

# This will update the dictionary
info.update({'age':20})

# This will add DOB
info.update({'DOB':2001})
print(info)

info.clear()
print(info)

info2={'name':'Karan','age':19,'eligible':True}
info2.pop('eligible')
print(info2)

del info2['age']
print(info2)

