data = (1, 2, 3, 2, 4, 1, 5, 3, 2, 1, 4, 4)
print("Tuple:", data)
unique_elements = set(data)   # get distinct elements
print("\nFrequency Table:")
print(f"{'Element':<10} {'Count'}")
print("-" * 18)
for elem in sorted(unique_elements):
    print(f"{elem:<10} {data.count(elem)}")
