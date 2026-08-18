days         = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
temperatures = (32.5, 33.1, 30.8, 29.4, 31.7, 34.2, 28.9)
print(f"{'Day':<12} {'Temp (C)'}")
print("-" * 22)
for day, temp in zip(days, temperatures):
    print(f"{day:<12} {temp}")
print(f"\nMax Temperature : {max(temperatures)} C")
print(f"Min Temperature : {min(temperatures)} C")
print(f"Avg Temperature : {sum(temperatures) / len(temperatures):.2f} C")
