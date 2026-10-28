from array import array

#1. append()
a = array('i', [10, 20, 30])
a.append(40)
print(a)

#2.extend()
a = array('i', [10, 20, 30])
a.extend([40, 50, 60])
print(a)

#3.insert()
a = array('i', [10, 20, 30])
a.insert(1, 15)
print(a)

#4.remove()
a = array('i', [10, 20, 30, 20])
a.remove(20)
print(a)

#5.pop()
a = array('i', [10, 20, 30])
x = a.pop()
print("Removed element:", x)
print("Array:", a)

#6.index()
a = array('i', [10, 20, 30, 40])
x = a.index(30)
print("Index:", x)

#7.count()
a = array('i', [10, 20, 10, 30, 10])
x = a.count(10)
print("Count:", x)

#8.reverse()
a = array('i', [10, 20, 30, 40])
a.reverse()
print(a)

#9.tolist()
a = array('i', [10, 20, 30])
b = a.tolist()
print("Array:", a)
print("List:", b)
