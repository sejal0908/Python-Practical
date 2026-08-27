# part A
# 1. Create an empty dictionary
inventory = {}

# 2. First product details
name1 = "Mobile Phone"
quantity1 = 5
price1 = 20000
year1 = 2020

# 3. Add first product to inventory
inventory["Product1"] = {
    "Name": name1,
    "Quantity": quantity1,
    "Price": price1,
    "Release Year": year1
}

# 4. Second product details
name2 = "Laptop"
quantity2 = 3
price2 = 50000
year2 = 2022

# 5. Add second product to inventory
inventory["Product2"] = {
    "Name": name2,
    "Quantity": quantity2,
    "Price": price2,
    "Release Year": year2
}

# 6. Display inventory
print("Inventory:")
print(inventory)

# 7. Check release years
print("Product1 Release Year:", inventory["Product1"]["Release Year"])
print("Product2 Release Year:", inventory["Product2"]["Release Year"])

# 8. Delete release years
del inventory["Product1"]["Release Year"]
del inventory["Product2"]["Release Year"]

print("After deleting release years:")
print(inventory)

#Part B

# Create tuple
prices = (250, 300, 150, 400, 100, 350, 200)

# Highest price
print("Highest price:", max(prices))

# Lowest price
print("Lowest price:", min(prices))

# Total sum
print("Total:", sum(prices))

# Sorted list
print("Sorted prices:", sorted(prices))

# Try to change a tuple element
prices[0] = 500