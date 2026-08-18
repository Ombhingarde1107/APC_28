cart = ["Milk","Bread","Rice"]
cart.append("Sugar")
cart.remove("Bread")
item = input("Search item: ")
if item in cart:
    print("Found")
else:
    print("Not Found")
print(cart)
print("Total Items:", len(cart))