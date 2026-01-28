#A class is a collection of objects. Classes are blueprints for creating objects.
#A class defines a set of attributes and methods that the created objects (instances) can have.
# Some points on Python class:  

# Classes are created by keyword class.
# Attributes are the variables that belong to a class.
# Attributes are always public and can be accessed using the dot (.) operator.
#  Example: Myclass.Myattribute

class Dog:

# class Dog: Defines a class named Dog.
# species: A class attribute shared by all instances of the class.
# __init__ method: Initializes the name and age attributes when a new object is created.

    species = "Canine"  # Class attribute
    # __init__: Special method used for initialization.
    # self.name and self.age: Instance attributes initialized in the constructor.
    def __init__(self, name, age):

        # Self parameter is a reference to the current instance of the class. 
        # It allows us to access the attributes and methods of the object.

        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

    def is_puppy(self):
        if self.age < 10:
            return ("its a puppy")
        else:return "not a puppy"

# State: It is represented by the attributes and reflects the properties of an object.
# Behavior: It is represented by the methods of an object and reflects the response of an object to other objects.
# Identity: It gives a unique name to an object and enables one object to interact with other objects.
dog1 = Dog("Buddy", 3)  # Create an instance of Dog
dog2 = Dog("Charlie", 13)  # Create another instance of Dog

# dog1 = Dog("Buddy", 3): Creates an object of the Dog class with name as "Buddy" and age as 3.
# dog1.name: Accesses the instance attribute name of the dog1 object.
# dog1.species: Accesses the class attribute species of the dog1 object.

print(dog1.name, dog1.age, dog1.species)  # Access instance and class attributes
print(dog2.name, dog2.age, dog2.species)  # Access instance and class attributes
print(Dog.species)  # Access class attribute directly


puppychecker = dog1.is_puppy()
print("dog one: ",puppychecker,"\ndog two: ",dog2.is_puppy())


class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = cat("Buddy", 3)
print(cat1.name)


# OOP assignment

# Import the math module to access mathematical functions like pi
import math

# Define a class called Circle to represent a circle
class Circle:
    # Initialize the Circle object with a given radius
    def __init__(self, radius):
        self.radius = radius
    
    # Calculate and return the area of the circle using the formula: π * r^2
    def calculate_circle_area(self):
        return math.pi * self.radius**2
    
    # Calculate and return the perimeter (circumference) of the circle using the formula: 2π * r
    def calculate_circle_perimeter(self):
        return 2 * math.pi * self.radius
