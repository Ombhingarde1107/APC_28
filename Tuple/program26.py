
tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (4, 5, 6, 7, 8, 9)
print("Tuple 1 :", tuple1)
print("Tuple 2 :", tuple2)
common = tuple(x for x in tuple1 if x in tuple2)
print("Common elements:", common)
