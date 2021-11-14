class enrollment:
    name ='No Name'
    Department = 'Department'
    DOB = 'DOB'
    place = 'Place'

print(enrollment.__dict__)

obj1 = enrollment()
obj1.name = 'ram'
obj1.Department = 'chem'
obj1.DOB = '2nd feb'
obj1.place = 'Jaipur'

attrs = vars(obj1)
# {'kids': 0, 'name': 'Dog', 'color': 'Spotted', 'age': 10, 'legs': 2, 'smell': 'Alot'}
# now dump this in some way or another
print(', '.join("%s: %s" % item for item in attrs.items()))

obj2 = enrollment()
# print obj2.bgroup
obj2.bgroup = 'o positive'
enrollment.bgroup = ''
print(enrollment.__dict__)
attrs = vars(obj2)
# {'kids': 0, 'name': 'Dog', 'color': 'Spotted', 'age': 10, 'legs': 2, 'smell': 'Alot'}
# now dump this in some way or another
print(', '.join("%s: %s" % item for item in attrs.items()))
obj3 = enrollment()
obj3.bgroup = 'o positive'

class box:
    bid=101
obj4 = box()

print obj4.bid    




