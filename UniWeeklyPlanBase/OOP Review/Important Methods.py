
class Book:
    """
    A simple class to represent a book.
    Demonstrates: __init__, __str__, __eq__, __lt__, __le__
    """
    
    def __init__(self, title, author, year):
        """
        -------------------------------------------------------
        CONSTRUCTOR - Creates a new Book object
        This method is called automatically when you create a Book.
        Use: my_book = Book("1984", "Orwell", 1949)
        -------------------------------------------------------
        Parameters:
            title - the book's title (str)
            author - the book's author (str)
            year - year published (int)
        -------------------------------------------------------
        """
        # Store the data in the object using self
        self.title = title
        self.author = author
        self.year = year
        return
    
    def __str__(self):
        """
        -------------------------------------------------------
        STRING METHOD - Returns a formatted string of the book
        This method is called automatically when you use print() or str()
        Use: print(my_book)
        -------------------------------------------------------
        Returns:
            A nicely formatted string with book information (str)
        -------------------------------------------------------
        """
        # Create a formatted string showing all the book's data
        string = f"'{self.title}' by {self.author} ({self.year})"
        return string
    
    def __eq__(self, other):
        """
        -------------------------------------------------------
        EQUALITY METHOD - Checks if two books are the same
        This method is called when you use == operator
        Use: if book1 == book2:
        -------------------------------------------------------
        Parameters:
            other - another Book to compare with (Book)
        Returns:
            True if books have same title and author, False otherwise (bool)
        -------------------------------------------------------
        """
        # Two books are equal if they have the same title and author
        result = (self.title == other.title and self.author == other.author)
        return result
    
    def __lt__(self, other):
        """
        -------------------------------------------------------
        LESS THAN METHOD - Determines if this book comes before another
        This method is called when you use < operator
        Use: if book1 < book2:
        -------------------------------------------------------
        Parameters:
            other - another Book to compare with (Book)
        Returns:
            True if this book comes before other, False otherwise (bool)
        -------------------------------------------------------
        """
        # Compare books by author name first, then by title
        # Using tuples is a Python shortcut for comparing multiple values
        result = (self.author.lower(), self.title.lower()) < \
                 (other.author.lower(), other.title.lower())
        return result
    
    def __le__(self, other):
        """
        -------------------------------------------------------
        LESS THAN OR EQUAL METHOD - Checks if book comes before or equals another
        This method is called when you use <= operator
        Use: if book1 <= book2:
        -------------------------------------------------------
        Parameters:
            other - another Book to compare with (Book)
        Returns:
            True if this book comes before or equals other, False otherwise (bool)
        -------------------------------------------------------
        """
        # A book is <= another if it's less than OR equal to it
        # We can use the methods we already defined!
        result = (self < other) or (self == other)
        return result


# ============================================================================
# DEMONSTRATION: Using all the methods
# ============================================================================

print("=" * 70)
print("BOOK CLASS DEMONSTRATION - All Methods Explained")
print("=" * 70)

# -----------------------------
# 1. __init__ - CONSTRUCTOR
# -----------------------------
print("\n1. CREATING BOOKS (using __init__ constructor)")
print("-" * 70)
print("Code: book1 = Book('1984', 'Orwell', 1949)")
book1 = Book("1984", "Orwell", 1949)
print("✓ Created book1")

print("\nCode: book2 = Book('Animal Farm', 'Orwell', 1945)")
book2 = Book("Animal Farm", "Orwell", 1945)
print("✓ Created book2")

print("\nCode: book3 = Book('1984', 'Orwell', 1949)")
book3 = Book("1984", "Orwell", 1949)
print("✓ Created book3 (same as book1)")

print("\nSummary: __init__ is called automatically when you create an object.")
print("         You pass the values, and it stores them using 'self'.")

# -----------------------------
# 2. __str__ - STRING METHOD
# -----------------------------
print("\n\n2. PRINTING BOOKS (using __str__ method)")
print("-" * 70)
print("Code: print(book1)")
print("Output:", book1)

print("\nCode: print(book2)")
print("Output:", book2)

print("\nCode: print(book3)")
print("Output:", book3)

print("\nSummary: __str__ is called automatically by print().")
print("         It returns a formatted string representation of the object.")

# -----------------------------
# 3. __eq__ - EQUALITY METHOD
# -----------------------------
print("\n\n3. COMPARING BOOKS FOR EQUALITY (using __eq__ method)")
print("-" * 70)
print(f"book1: {book1}")
print(f"book2: {book2}")
print(f"book3: {book3}")

print("\nCode: book1 == book2")
result = book1 == book2
print(f"Result: {result}")
print("Explanation: Different books by same author, so False")

print("\nCode: book1 == book3")
result = book1 == book3
print(f"Result: {result}")
print("Explanation: Same title and author, so True")

print("\nCode: book1 != book2")
result = book1 != book2
print(f"Result: {result}")
print("Explanation: != is automatically the opposite of ==, so True")

print("\nSummary: __eq__ is called when you use == or !=")
print("         It compares objects based on the logic you define.")

# -----------------------------
# 4. __lt__ - LESS THAN METHOD
# -----------------------------
print("\n\n4. ORDERING BOOKS (using __lt__ method)")
print("-" * 70)
print(f"book1: {book1}")
print(f"book2: {book2}")

print("\nCode: book1 < book2")
result = book1 < book2
print(f"Result: {result}")
print("Explanation: Comparing 'Orwell, 1984' < 'Orwell, Animal Farm'")
print("             Since authors are equal, compare titles: '1984' < 'Animal Farm' = True")

print("\nCode: book2 < book1")
result = book2 < book1
print(f"Result: {result}")
print("Explanation: 'Animal Farm' < '1984' = False")

print("\nCode: book1 >= book2")
result = book1 >= book2
print(f"Result: {result}")
print("Explanation: >= is automatically the opposite of <, so False")

print("\nSummary: __lt__ is called when you use < or >=")
print("         It determines the sorting order of objects.")

# -----------------------------
# 5. __le__ - LESS THAN OR EQUAL METHOD
# -----------------------------
print("\n\n5. LESS THAN OR EQUAL (using __le__ method)")
print("-" * 70)
print(f"book1: {book1}")
print(f"book2: {book2}")
print(f"book3: {book3}")

print("\nCode: book1 <= book2")
result = book1 <= book2
print(f"Result: {result}")
print("Explanation: book1 < book2 is True, so book1 <= book2 is True")

print("\nCode: book1 <= book3")
result = book1 <= book3
print(f"Result: {result}")
print("Explanation: book1 == book3 is True, so book1 <= book3 is True")

print("\nCode: book2 <= book1")
result = book2 <= book1
print(f"Result: {result}")
print("Explanation: book2 < book1 is False and book2 == book1 is False, so False")

print("\nCode: book2 > book1")
result = book2 > book1
print(f"Result: {result}")
print("Explanation: > is automatically the opposite of <=, so True")

print("\nSummary: __le__ is called when you use <= or >")
print("         It combines the logic of < and ==")

# -----------------------------
# 6. SORTING (uses __lt__ and __eq__)
# -----------------------------
print("\n\n6. SORTING A LIST OF BOOKS (uses __lt__ automatically)")
print("-" * 70)

book4 = Book("Brave New World", "Huxley", 1932)
book5 = Book("Fahrenheit 451", "Bradbury", 1953)

books = [book1, book2, book4, book5, book3]

print("Before sorting:")
for i, book in enumerate(books):
    print(f"  {i}: {book}")

books.sort()

print("\nAfter sorting (by author, then title):")
for i, book in enumerate(books):
    print(f"  {i}: {book}")

print("\nSummary: Python's sort() uses __lt__ to compare objects.")
print("         Objects are sorted based on your __lt__ logic.")

# -----------------------------
# FINAL SUMMARY
# -----------------------------
print("\n" + "=" * 70)
print("COMPLETE SUMMARY OF ALL METHODS")
print("=" * 70)
print("""
1. __init__(self, ...)
   - CONSTRUCTOR: Creates the object and stores its data
   - Called: Automatically when you write Book(...)
   - Purpose: Initialize object attributes

2. __str__(self)
   - STRING METHOD: Returns a readable string representation
   - Called: Automatically by print() or str()
   - Purpose: Display object in a human-readable format

3. __eq__(self, other)
   - EQUALITY METHOD: Checks if two objects are equal
   - Called: When you use == or !=
   - Purpose: Define what makes two objects "the same"

4. __lt__(self, other)
   - LESS THAN METHOD: Checks if one object comes before another
   - Called: When you use < or >=
   - Purpose: Define the sorting order

5. __le__(self, other)
   - LESS THAN OR EQUAL METHOD: Checks if one object comes before or equals another
   - Called: When you use <= or >
   - Purpose: Combine equality and ordering logic

KEY POINTS:
- These are called "magic methods" (double underscores)
- You define them, but Python calls them automatically
- They let you use operators (==, <, <=) with your objects
- Python automatically provides opposites (!=, >=, >)
""")

print("=" * 70)
print("END OF DEMONSTRATION")
print("=" * 70)




# Why Can't We Just Use Normal Operators?
# The Problem:
# Python doesn't know HOW to compare YOUR objects!

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Create two students
alice = Student("Alice", 85)
bob = Student("Bob", 90)

# Try to use "normal" operators
print(alice < bob)  

# ERROR! Python doesn't know what this means!


# **Error you get:**
# ```
# TypeError: '<' not supported between instances of 'Student' and 'Student'