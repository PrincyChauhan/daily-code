# you are given a grocery list which consists of three parameters
# items, quantity,price
# your task is to find 
# ---> higher selling item
# ---> Total selling item
# ---> Avg selling item

# ---> 2 decimal points

# input --> 3 
# apple ,1.0,5
# orange,10.0,5
# apple,10.0,5

# output apple,10.5, 35.0
# Input
n = int(input())  # Number of items

items = []
quantities = []
prices = []

# Collect all inputs
for _ in range(n):
    item = input()
    quantity = float(input())
    price = float(input())
    items.append(item)
    quantities.append(quantity)
    prices.append(price)

# Initialize variables
max_item = ""
max_quantity = 0.0
total_price = 0.0

# Brute-force calculation for each item
for i in range(n):
    current_item = items[i]
    current_quantity = 0.0
    current_total_price = 0.0

    # Calculate total quantity and price for the current item
    for j in range(n):
        if items[j] == current_item:
            current_quantity += quantities[j]
            current_total_price += quantities[j] * prices[j]

    # Update the item with the highest quantity sold
    if current_quantity > max_quantity:
        max_item = current_item
        max_quantity = current_quantity
        total_price = current_total_price

# Calculate the average selling price for the highest selling item
average_price = total_price / max_quantity

# Output the result
print(f"{max_item},{max_quantity:.2f},{total_price:.2f}")