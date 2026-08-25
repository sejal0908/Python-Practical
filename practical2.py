# 1. Create an empty list
shopping_list = []

# 2. Store the items in the shopping list
shopping_list = ["Watch", "Laptop", "Shoes", "Pen", "Clothes"]

# 3. Add new item Football to the shopping list
shopping_list.append("Football")

# 4. Print the last item from the shopping list
print("Last item:", shopping_list[-1])

# 5. Print the entire shopping list
print("Shopping List:", shopping_list)

# 6. Print the important items like Laptop and Shoes
print("Important items:", shopping_list[1], "and", shopping_list[2])

# 7. Change Pen to Notebook
shopping_list[3] = "Notebook"

# 8. Delete the least important item (Clothes)
shopping_list.remove("Clothes")

# Print the final shopping list
print("Final Shopping List:", shopping_list)