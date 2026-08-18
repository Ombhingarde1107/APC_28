tuple_a = (1, 2, 3, 4, 5)
tuple_b = (3, 4, 5, 6, 7)
merged = tuple_a + tuple_b
print("Merged (with duplicates)   :", merged)
unique = tuple(dict.fromkeys(merged))
print("Merged (without duplicates):", unique)
