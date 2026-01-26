# CP164: Data Structures I - Week 1 Study Plan
## Winter 2026 - Teacher's Guide

---

## **Week 1 Overview: Introduction to Classes, Objects, and Data Structures**

### **Learning Outcomes**
By the end of Week 1, students should be able to:
- Explain the concepts of classes and objects
- Define and develop classes in Python
- Use a class in Python including instantiating objects
- Define and use methods for a class
- Explain and define ADT (Abstract Data Type) and data structure
- Articulate the differences between data structures and ADTs
- Describe approaches for implementing ADTs and data structures in Python

---

## **Required Tasks for Students**
1. Read Lesson 1 in full
2. Complete Lab 1 tasks
3. Read and complete Assignment 1
4. Submit Assignment 1 to MyLearningSpace Dropbox

---

## **Lecture 1: Classes and Objects in Python**

### **Topics to Cover:**

#### 1. **Introduction to Object-Oriented Programming (30 min)**
- **Concept of Classes and Objects**
  - Classes as templates/blueprints
  - Objects as instances of classes
  - Properties (attributes) vs Behaviors (methods)
  
- **Real-World Analogy: The Car Example**
  - Class: Car (general template)
  - Properties: Make, Model, Year, Color
  - Methods: Start(), Stop(), Move(), Accelerate()
  - Objects: Specific cars (BMW 2000 M3 white, Honda 1998 Civic red)

- **Another Example: Person Class**
  - Attributes: name, gender, birth_date, birth_place
  - Methods: initialize(), get_first_name(), get_birth_date(), set_birth_date()

#### 2. **Categories of Class Methods (20 min)**
Explain the four types of methods:
- **Constructors**: Initialize new instances (e.g., `__init__`)
- **Accessors (getters)**: Return attribute values
- **Mutators (setters)**: Modify attribute values
- **Iterators**: Traverse contents sequentially

#### 3. **Public vs Private in Python (15 min)**
- **Concept Overview:**
  - User of a class vs Designer of a class
  - Public: accessible by anyone
  - Private: accessible only within the class
  
- **Python Naming Convention:**
  - Attributes/methods starting with `_` or `__` are treated as private
  - This is a convention, not enforcement
  - Programmers should respect this convention

---

## **Lecture 2: Defining Classes in Python**

### **Topics to Cover:**

#### 1. **Minimum Class Definition (20 min)**
```python
class Name:
    def __init__(self[, param,]):
        ...
```

**Key Points:**
- Class name
- Constructor method `__init__`
- The `self` parameter (always first, never passed as argument)
- Class methods must be indented

#### 2. **The Number Class Example (20 min)**
Walk through complete example:
```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def square(self):
        answer = self.value * self.value
        return answer
```

**Teaching Points:**
- Class attributes defined in constructor
- Using `self.attribute` syntax
- Creating objects: `example = Number(5)`
- Calling methods: `answer = example.square()`

#### 3. **Importing and Using Classes (10 min)**
```python
from Number import Number
example = Number(0)
```

#### 4. **Accessing Attributes (10 min)**
```python
print(example.value)
example.value = 0
example.value = int(input("Enter a new value: "))
```

---

## **Lecture 3: The Student Class - Comprehensive Example**

### **Topics to Cover:**

#### 1. **Student Class Structure (20 min)**
- **Attributes:**
  - student_id (9-digit string)
  - surname
  - forename
  - birth_date (YYYY-MM-DD format)

- **Assertion Statements in Constructor:**
  ```python
  assert len(student_id) == 9 and student_id.isdigit(), \
      "Student ID must be a 9 digit string"
  ```
  - Purpose: Validate input data
  - Error handling demonstration

#### 2. **Magic Methods (40 min)**

**a) The `__init__` Constructor**
- Creating Student objects
- Passing parameters vs arguments
- The `self` parameter

**b) The `__str__` Method**
- Returns formatted string representation
- Used with print() and str()
- Demonstration: What happens without `__str__`?
  - Shows object memory address: `<__main__.Student object at 0x023C74B0>`

**c) The `__eq__` Method**
- Enables `==` operator
- Compares student_id only
- Python automatically provides `!=`

**d) The `__lt__` Method**
- Enables `<` operator (and `>=` automatically)
- Comparison logic: surname → forename → student_id
- Tuple comparison shortcut:
  ```python
  result = (self.surname.lower(), self.forename.lower(), self.student_id) < \
           (target.surname.lower(), target.forename.lower(), target.student_id)
  ```

**e) The `__le__` Method**
- Enables `<=` operator (and `>` automatically)
- Uses previously defined methods:
  ```python
  result = (self == target or self < target)
  ```

#### 3. **Practical Methods (15 min)**
- `login()`: Generate network login
- `email()`: Generate email address
- `write()`: Write to file

**Key Teaching Point:** With all comparison methods defined, Student objects can be sorted using Python's built-in sort()

---

## **Lab Session 1: Hands-On Practice**

### **Lab Activities (2.5 hours):**

#### **Activity 1: Working with the Number Class (30 min)**
Students should:
1. Create Number.py module
2. Implement the Number class
3. Create test program to:
   - Create Number objects
   - Call the square() method
   - Access and modify the value attribute

#### **Activity 2: Student Class Exploration (45 min)**
Students should:
1. Import and use the Student class
2. Create multiple Student objects
3. Test comparison operators
4. Sort a list of Students
5. Generate logins and emails
6. Handle assertion errors (intentionally create invalid objects)

#### **Activity 3: Introduction to Food Class (45 min)**
Students begin working with:
- Static variables (ORIGIN constant)
- Static methods (@staticmethod decorator)
- Understanding class-level vs instance-level attributes

---

## **Lecture 4: Data Storage Classes**

### **Topics to Cover:**

#### 1. **The Food Class (45 min)**

**a) Food Attributes:**
- name (str)
- origin (int - index into ORIGIN list)
- is_vegetarian (boolean)
- calories (int ≥ 0)

**b) Static Attributes:**
```python
ORIGIN = ("Canadian", "Chinese", "Indian", "Ethiopian",
          "Mexican", "Greek", "Japanese", "Italian", "American",
          "Scottish", "New Zealand", "English")
```
- Defined outside `__init__`
- Shared by all instances
- Saves memory
- Enforces consistency

**c) The `@staticmethod` Decorator:**
```python
@staticmethod
def origins():
    # Can be called as Food.origins()
    # No object needed
```

**d) Assertion Statements:**
```python
assert origin in range(len(Food.ORIGIN)), "Invalid origin ID"
assert is_vegetarian in (True, False, None), "Must be True or False"
assert calories is None or calories >= 0, "Calories must be >= 0"
```

#### 2. **The Movie Class Overview (30 min)**

**a) Movie Constants:**
- MIN_RATING = 0
- MAX_RATING = 10
- FIRST_YEAR = 1888
- GENRES (tuple of genre names)
- GENRE_CODES (range of valid codes)

**b) Movie Attributes:**
- title (str)
- year (int, ≥ 1888)
- director (str)
- rating (float, 0-10)
- genres (list of int)

**c) Comparison Logic:**
Movies sorted by title, then year
- "Zulu, 1964" comes before "Zulu, 2013"

---

## **Lecture 5: Data Structures and Abstract Data Types**

### **Topics to Cover:**

#### 1. **What is a Data Structure? (20 min)**
- Definition: Mechanism to store and manipulate data efficiently
- Examples: arrays, linked lists, binary search trees, heaps, graphs, hash tables
- Purpose: Organize data for efficient operations
- Python built-ins: lists and tuples

#### 2. **What is an Abstract Data Type (ADT)? (25 min)**

**Definition:**
- Collection of data + set of operations
- Describes WHAT, not HOW
- Behavior from user's perspective
- Implementation-independent

**Key Characteristics:**
- **Modularity**: Well-designed, testable components
- **Information Hiding**: Internal mechanisms hidden from users
- **Interface**: Visible methods for users
- **Encapsulation**: Grouping entity + methods together

#### 3. **Example: Priority Queue ADT (30 min)**

**Real-World Analogy: Hospital Emergency Room**
- Collection of prioritized items (patients)
- Removed by priority (severity)
- New items added anytime
- Equal priority → FIFO order

**Priority Queue Methods:**
- Initialize: Create empty queue
- Size: Return number of items
- Is Empty: Check if empty
- Add: Insert new item
- Remove: Remove highest priority item
- Peek: View highest priority without removing

#### 4. **ADTs vs Data Structures (20 min)**

**Similarities:**
- Both hold multiple data items
- Both organize data

**Differences:**

| ADT | Data Structure |
|-----|----------------|
| Abstract concept | Concrete implementation |
| Describes functionality | Specifies storage method |
| What operations exist | How operations work |
| User perspective | Implementation details |

**Visual Representation:**
```
Application Program
        ↓
    [Interface]
   Public Methods
        ↓
      [ADT]
        ↓
   Private Methods
   Data Structures
```

**Key Point:** User doesn't know/care about implementation, but implementation affects performance.

**Car Analogy:**
- Car = ADT
- Driver = User of ADT
- Engine = Data Structure
- Driver uses same interface (steering, pedals) regardless of engine type
- Engine can be replaced without driver retraining

---

## **Important Teaching Points Throughout Week 1:**

### **Recurring Concepts to Emphasize:**

1. **The `self` Parameter:**
   - Always first parameter in methods
   - Never passed as argument when calling
   - Used to access class attributes/methods

2. **Object Creation:**
   - Only through constructors
   - String of data ≠ Object
   - Must call constructor with proper parameters

3. **Magic Methods:**
   - Double underscore naming
   - Not called by name
   - Enable Python operators/functions

4. **Naming Conventions:**
   - Module name = Class name
   - UPPERCASE for constants
   - `_` or `__` prefix for private
   - lowercase_with_underscores for variables/functions

5. **Documentation:**
   - Every method needs docstring
   - Include Use:, Parameters:, Returns: sections
   - Examples help clarity

---

## **Lab 1 Detailed Tasks**

### **Task 1: Number Class Implementation**
Students create a working Number class with:
- Constructor accepting a value
- square() method
- cube() method (add this)
- Test program demonstrating all functionality

### **Task 2: Student Class Usage**
Students write programs that:
- Create 5+ Student objects
- Sort them
- Generate logins/emails for all
- Write to file
- Read from file (if covered)

### **Task 3: Food Class Basics**
Students work with Food class:
- Create Food objects with different origins
- Test comparison operators
- Implement origins() static method
- Implement __str__() method
- Test with various data

---

## **Assignment 1 Overview**

Students should implement:
1. Complete any incomplete methods in Food class
2. Complete any incomplete methods in Movie class
3. Create test programs for both classes
4. Demonstrate understanding of:
   - Object creation
   - Method calling
   - Comparisons
   - Static methods
   - File I/O with objects

---

## **Common Student Challenges & Solutions**

### **Challenge 1: Understanding `self`**
**Problem:** Students forget `self` or pass it as argument
**Solution:** 
- Use car analogy: "self" means "this car"
- Show side-by-side: definition vs calling
- Practice reading error messages

### **Challenge 2: Magic Method Names**
**Problem:** Students try to call `__str__` directly
**Solution:**
- Emphasize "magic" = automatic
- Show the "Use:" line in docstrings
- Demonstrate both styles (works vs doesn't work)

### **Challenge 3: Assertion Errors**
**Problem:** Students don't understand assertion purpose
**Solution:**
- Intentionally trigger assertions
- Read error messages together
- Explain validation importance

### **Challenge 4: ADT vs Data Structure Confusion**
**Problem:** Students mix up abstract vs concrete
**Solution:**
- Use multiple analogies (car, blueprint/house)
- Create comparison table
- Ask "what vs how" questions

### **Challenge 5: Import Errors**
**Problem:** Module naming or location issues
**Solution:**
- Verify module name = class name
- Check file location in project
- Show Eclipse/IDE organization

---

## **Assessment Checkpoints for Week 1**

By end of week, students should demonstrate:

✓ Ability to create simple classes
✓ Understanding of constructors
✓ Proper use of `self`
✓ Implementation of magic methods
✓ Object instantiation
✓ Method calling
✓ Understanding public vs private
✓ Ability to work with provided classes (Student, Food, Movie)
✓ Conceptual understanding of ADT vs data structure

---

## **Week 1 Summary Points**

### **Key Takeaways:**
1. Classes are templates; objects are instances
2. Every method needs `self` as first parameter
3. Magic methods enable Python operators
4. ADTs describe functionality; data structures implement it
5. Users interact with interface; implementation is hidden
6. Python uses naming conventions for public/private
7. Static methods/attributes exist at class level
8. Proper validation (assertions) prevents bad data

### **Looking Ahead to Week 2:**
- Review of arrays and linked lists concepts
- Beginning algorithm analysis
- Introduction to Big O notation
- Building toward first data structure implementations

---

## **Resources for Teaching Week 1**

### **Code Examples Provided:**
- Number.py (simple example)
- Student.py (comprehensive example)
- Food.py (data storage with statics)
- Movie.py (complex data storage)

### **Visual Aids to Create:**
- Class vs Object diagram
- Car analogy illustration
- Public/Private access diagram
- ADT vs Data Structure relationship diagram
- Emergency room priority queue illustration

### **Recommended Activities:**
- Live coding demonstrations
- Interactive Eclipse/PyDev walkthrough
- Group discussion on real-world ADTs
- Pair programming for lab exercises

### **Additional Practice:**
- Create a Book class
- Create a Person class with relationships
- Implement a Product class for a store
- Design a Vehicle inheritance hierarchy (preview for later)

---

## **Office Hours Discussion Topics**

Common questions to prepare for:
1. "Why do we need classes?"
2. "When do I use `self`?"
3. "What's the difference between method and function?"
4. "Why can't I access private attributes?"
5. "How do I know which magic methods to implement?"
6. "What's the point of assertions?"
7. "Why learn ADTs if data structures do the work?"

---

**End of Week 1 Study Plan**
