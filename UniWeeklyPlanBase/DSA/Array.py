# An array is a collection of items of the same variable type that are stored at contiguous memory locations. 
# It is one of the most popular and simple data structures used in programming.

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

# Types of Arrays on the basis of "Size"

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



# Python program to find second largest element in an array
# using Sorting


# Types of Arrays on the basis of Dimensions

# One-dimensional Array(1-D Array): You can imagine a 1d array as a row, where elements are stored one after another.
arrM1 = [1,2,1,2]

#┌───┐┌───┐┌───┐┌───┐
#│ 1 ││ 2 ││ 1 ││ 2 │
#└───┘└───┘└───┘└───┘
#  0    1    2    3   


# 2. Multi-dimensional Array: A multi-dimensional array is an array with more than one dimension. We can use multidimensional array to store complex data 
# in the form of tables, etc. We can have 2-D arrays, 3-D arrays, 4-D arrays and so on.

# Two-Dimensional Array(2-D Array or Matrix): 2-D Multidimensional arrays can be considered as an array of arrays or as a matrix consisting of rows and columns.

arrM2 = [[1,2,1,2],
         [1,3,1,2],
         [1,2,1,2]]

# 0    1    2    3
#┌───┐┌───┐┌───┐┌───┐
#│ 1 ││ 2 ││ 1 ││ 2 │  0
#└───┘└───┘└───┘└───┘  
#┌───┐┌───┐┌───┐┌───┐
#│ 1 ││ 3 ││ 1 ││ 2 │  1
#└───┘└───┘└───┘└───┘ 
#┌───┐┌───┐┌───┐┌───┐
#│ 1 ││ 2 ││ 1 ││ 2 │  2
#└───┘└───┘└───┘└───┘  

#Acsessing:
# 1D:
print("One dementional array acsess of index" ,arrM1[1])
#D2
print("Acsessing specific element of the matrix:",arrM2[1][1])
print("Two dementional Row Acsess:",arrM2[1])
column = int(input())
for i in range(0,len(arrM2)):
    print(arrM2[i][column])

# Three-Dimensional Array(3-D Array): A 3-D Multidimensional array contains three dimensions, so it can be considered an array of two-dimensional arrays.

