numbers = [1,2,3,4,5]
left = numbers[1:] + [numbers[0]]
right = [numbers[-1]] + numbers[:-1]
print("Left:", left)
print("Right:", right)