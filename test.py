#####################################################################
# author:       anky
# date:         17th Jan, 2023.
# description:  A file to test out the Item class and its subclasses.
#####################################################################

# Import all the classes from the file named SaleItem.py
from main import *

# Create 3 basic items and print them
i1 = Item("bananas", 2, 4.59)
i2 = Item("jeans", 30, 44.99)
i3 = Item("shirt", 20, 29.99)

print("Item\tCost\tPrice\tExtra Info")
print("-" * 50)
print(i1)
print(i2)
print(i3)
print("-" * 50)

# Create Clothing and Food items and print them
c1 = Clothing("jeans", "Levis", 30, 44.99, 32)
c2 = Clothing("shirt", "Macy's", 20, 29.99, 16)
f1 = Food("bananas", 2, 4.59)
f2 = Food("Avocado", 1.50, 5.50)
f2.shelfLife = 2

print(c1)
print(c2)
print(f1)
print(f2)
print("-" * 50)

# Create Shoes and Chips and print them
s1 = Shoe(59.99, 89.99, 10)
s2 = Shoe(49.99, 79.99, 4)
h1 = Chips()

print(s1)
print(s2)
print(h1)
print("-" * 50)

# Testing out the range checking
h1.shelfLife = -5
s2.size = -2

print(s2)
print(h1)
print("-" * 50)
