# An array is a collection of items of the same variable type that are stored at contiguous memory locations. It is one of the most popular and simple data structures used in programming.

# Array Element: Elements are items stored in an array.
# Array Index: Elements are accessed by their indexes. Indexes in most of the programming languages start from 0. 

# Initilizaion:

# This list will store integer type elements
arr = [1, 2, 3, 4, 5]

# This list will store character type elements (strings in Python)
arr = ['a', 'b', 'c', 'd', 'e']

# This list will store float type elements
arr = [1.4, 2.0, 24.0, 5.0, 0.0]  # All float values

# ----------------------------------------------------------
# In C++:
# // This array will store integer type element
# int arr[5];      

# // This array will store char type element
# char arr[10];   

# // This array will store float type element
# float arr[20];  
# ----------------------------------------------------------

# Types of Arrays on the basis of Size
# 1. Fixed Sized Arrays

# Create a fixed-size list of length 5, 
# initialized with zeros
arrF = [0] * 5

# Output the fixed-size list
print(arrF)

# 2. Dynamic Sized Arrays
# Dynamic Array
arrD = []
arrD.append(2)
arrD.append(3)
print(arrD)