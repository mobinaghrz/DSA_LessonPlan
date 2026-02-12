#Definition: Stack is a linear data structure in which insertion and deletion are done at one end this end is generally called the top. 
# It works on the principle of Last In First Out (LIFO) or First in Last out (FILO). 
# LIFO means the last element inserted inside the stack is removed first. FILO means, 
# the last inserted element is available first and is the first one to be deleted.


# LIFO(Last In First Out) Principle
# The LIFO principle means that the last element added to a stack is the first one to be removed.

# New elements are always pushed on top.
# Removal (pop) also happens only from the top.
# This ensures a strict order: last in → first out.


# Just use a list - it has push/pop
stack = []
stack.append(1)  # push
stack.pop()      # pop



# Build a proper Stack CLASS
class Stack:
    def __init__(self):
        self._data = []  # Hidden implementation
    
    def push(self, value):
        self._data.append(value)
    
    def pop(self):
        if not self.is_empty():
            return self._data.pop()
    
    def is_empty(self):
        return len(self._data) == 0

# Now use YOUR stack
my_stack = Stack()
my_stack.push(10)

"""
-------------------------------------------------------
Stack Methods - Simple Demonstration
Shows all basic Stack methods with clear examples
-------------------------------------------------------
"""

# =============================================================================
# STACK CLASS DEFINITION
# =============================================================================

class Stack:
    """
    Stack ADT - Last In, First Out (LIFO)
    Implements all required stack methods
    """
    
    def initialize(self):
        """
        Creates an empty stack
        Use: stack.initialize()
        """
        self._data = []
        print("✓ Stack initialized (empty)")
    
    def __init__(self):
        """Constructor - automatically calls initialize"""
        self.initialize()
    
    def push(self, value):
        """
        Adds value to the top of the stack
        Use: stack.push(value)
        Parameters:
            value - data to add to stack
        """
        self._data.append(value)
        print(f"Pushed: {value}")
    
    def pop(self):
        """
        Removes and returns the value on top of the stack
        Use: value = stack.pop()
        Returns:
            value - the top item, or None if stack is empty
        """
        if self.is_empty():
            print("⚠ Cannot pop - stack is empty!")
            return None
        
        value = self._data.pop()
        print(f"Popped: {value}")
        return value
    
    def peek(self):
        """
        Returns a copy of the value at the top without removing it
        Use: value = stack.peek()
        Returns:
            value - copy of top item, or None if stack is empty
        """
        if self.is_empty():
            print("⚠ Cannot peek - stack is empty!")
            return None
        
        value = self._data[-1]  # Get last item (top of stack)
        print(f"Peeked: {value}")
        return value
    
    def is_empty(self):
        """
        Checks if the stack is empty
        Use: if stack.is_empty():
        Returns:
            True if stack has no items, False otherwise
        """
        result = len(self._data) == 0
        print(f"Is empty? {result}")
        return result
    
    def __iter__(self):
        """
        Iterator - allows looping through stack from top to bottom
        Use: for item in stack:
        """
        # Iterate from top to bottom (reverse order)
        for i in range(len(self._data) - 1, -1, -1):
            yield self._data[i]
    
    def __str__(self):
        """String representation for debugging"""
        if self.is_empty():
            return "Stack: []"
        return f"Stack: {self._data} (top -> {self._data[-1]})"


# =============================================================================
# EXAMPLE 1: BASIC STACK OPERATIONS
# =============================================================================

print("=" * 80)
print("EXAMPLE 1: BASIC STACK OPERATIONS")
print("=" * 80)

# 1. INITIALIZE - Create empty stack
print("\n--- 1. Initialize ---")
stack = Stack()

# 2. IS_EMPTY - Check if empty
print("\n--- 2. Is Empty (on empty stack) ---")
stack.is_empty()

# 3. PUSH - Add items to stack
print("\n--- 3. Push items ---")
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

# 4. IS_EMPTY - Check if empty again
print("\n--- 4. Is Empty (on filled stack) ---")
stack.is_empty()

# 5. PEEK - Look at top without removing
print("\n--- 5. Peek at top ---")
top_value = stack.peek()
print(f"Top value is: {top_value}")
stack.peek()  # Can peek multiple times
print("Note: Item still on stack after peeking")

# 6. POP - Remove items from stack
print("\n--- 6. Pop items ---")
value1 = stack.pop()
value2 = stack.pop()
print(f"Retrieved values: {value1}, {value2}")

# 7. PEEK after POP
print("\n--- 7. Peek after popping ---")
stack.peek()

# 8. POP all remaining items
print("\n--- 8. Pop remaining items ---")
stack.pop()
stack.pop()

# 9. Try operations on empty stack
print("\n--- 9. Operations on empty stack ---")
stack.is_empty()
stack.peek()  # Returns None
stack.pop()   # Returns None


# =============================================================================
# EXAMPLE 2: REAL-WORLD SCENARIO - BROWSER HISTORY
# =============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 2: BROWSER HISTORY (Real-World Example)")
print("=" * 80)

browser_history = Stack()

# User visits websites
print("\n--- User visits websites (push) ---")
browser_history.push("google.com")
browser_history.push("youtube.com")
browser_history.push("facebook.com")
browser_history.push("twitter.com")

# Check current page
print("\n--- Check current page (peek) ---")
current_page = browser_history.peek()
print(f"📄 Currently viewing: {current_page}")

# Press back button (pop)
print("\n--- Press back button 2 times (pop) ---")
browser_history.pop()
browser_history.pop()

# Check current page again
print("\n--- Check current page again (peek) ---")
current_page = browser_history.peek()
print(f"📄 Currently viewing: {current_page}")

# Check if history exists
print("\n--- Check if history exists (is_empty) ---")
has_history = not browser_history.is_empty()
print(f"Can go back? {has_history}")


# =============================================================================
# EXAMPLE 3: UNDO FUNCTIONALITY
# =============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 3: UNDO FUNCTIONALITY (Text Editor)")
print("=" * 80)

undo_stack = Stack()

# User types text
print("\n--- User types text (push) ---")
undo_stack.push("Typed: Hello")
undo_stack.push("Typed: World")
undo_stack.push("Typed: !")
undo_stack.push("Deleted: !")
undo_stack.push("Typed: Python")

# Check last action
print("\n--- Check last action (peek) ---")
last_action = undo_stack.peek()
print(f"⌨️  Last action: {last_action}")

# User presses UNDO
print("\n--- User presses UNDO (pop) ---")
undone_action = undo_stack.pop()
print(f"🔙 Undoing: {undone_action}")

# Check what the current state is
print("\n--- Check current action (peek) ---")
current_action = undo_stack.peek()
print(f"⌨️  Current state: {current_action}")


# =============================================================================
# EXAMPLE 4: PLATE STACK
# =============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 4: STACK OF PLATES (Classic Example)")
print("=" * 80)

plates = Stack()

# Stack plates
print("\n--- Stacking plates (push) ---")
plates.push("Blue Plate")
plates.push("Red Plate")
plates.push("Green Plate")
plates.push("Yellow Plate")

# Check top plate
print("\n--- Check top plate (peek) ---")
top_plate = plates.peek()
print(f"🍽️  Top plate: {top_plate}")

# Take plates (from top only!)
print("\n--- Taking plates (pop) ---")
plate1 = plates.pop()
plate2 = plates.pop()
print(f"Took: {plate1}, {plate2}")

# Check what's on top now
print("\n--- Check top plate again (peek) ---")
plates.peek()

# Check if plates remain
print("\n--- Check if plates remain (is_empty) ---")
if not plates.is_empty():
    print("✓ More plates available")


# =============================================================================
# EXAMPLE 5: ITERATOR - VIEWING ALL ITEMS
# =============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 5: ITERATOR - View All Items (Top to Bottom)")
print("=" * 80)

# Create stack with items
demo_stack = Stack()
print("\n--- Creating stack ---")
demo_stack.push("Bottom Item")
demo_stack.push("Middle Item")
demo_stack.push("Top Item")

# Use iterator to view all items
print("\n--- Iterating through stack (top to bottom) ---")
print("Items in stack:")
for item in demo_stack:
    print(f"  → {item}")

print("\nNote: Iterator is mainly for debugging")
print("      Normal use only accesses the TOP item")


# =============================================================================
# EXAMPLE 6: COMPLETE WORKFLOW
# =============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 6: COMPLETE WORKFLOW - All Methods in Order")
print("=" * 80)

print("\n--- Step 1: Initialize ---")
workflow_stack = Stack()

print("\n--- Step 2: Check if empty ---")
workflow_stack.is_empty()  # True

print("\n--- Step 3: Push items ---")
workflow_stack.push("First")
workflow_stack.push("Second")
workflow_stack.push("Third")

print("\n--- Step 4: Check if empty again ---")
workflow_stack.is_empty()  # False

print("\n--- Step 5: Peek at top ---")
top = workflow_stack.peek()

print("\n--- Step 6: Pop an item ---")
removed = workflow_stack.pop()

print("\n--- Step 7: Peek again (top changed) ---")
new_top = workflow_stack.peek()

print("\n--- Step 8: Iterate through remaining items ---")
print("Remaining items (top to bottom):")
for item in workflow_stack:
    print(f"  → {item}")


# =============================================================================
# EXAMPLE 7: ERROR HANDLING - Empty Stack Operations
# =============================================================================

print("\n" + "=" * 80)
print("EXAMPLE 7: ERROR HANDLING - Operations on Empty Stack")
print("=" * 80)

empty_stack = Stack()

print("\n--- Trying to pop from empty stack ---")
result = empty_stack.pop()
print(f"Result: {result}")

print("\n--- Trying to peek at empty stack ---")
result = empty_stack.peek()
print(f"Result: {result}")

print("\n--- Checking if empty ---")
empty_stack.is_empty()


# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "=" * 80)
print("SUMMARY: STACK METHODS")
print("=" * 80)

print("""
╔════════════════════════════════════════════════════════════════╗
║                    STACK METHOD SUMMARY                        ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  initialize()     → Create empty stack                        ║
║  push(value)      → Add item to TOP                           ║
║  pop()            → Remove and return item from TOP           ║
║  peek()           → View TOP item (without removing)          ║
║  is_empty()       → Check if stack has no items               ║
║  __iter__()       → Loop through items (top to bottom)        ║
║                                                                ║
╠════════════════════════════════════════════════════════════════╣
║  REMEMBER: LIFO - Last In, First Out                          ║
║            Like a stack of plates!                            ║
╚════════════════════════════════════════════════════════════════╝

REAL-WORLD EXAMPLES:
  • Browser back button     → pop() from history
  • Text editor undo        → pop() from action stack
  • Stack of plates         → push() and pop() from top
  • Function call stack     → push() when calling, pop() when returning

KEY RULES:
  ✓ Always add/remove from TOP only
  ✓ peek() doesn't remove the item
  ✓ pop() removes AND returns the item
  ✓ Check is_empty() before pop/peek to avoid errors
  ✓ Iterator is mainly for debugging
""")

print("=" * 80)
print("END OF STACK DEMONSTRATION")
print("=" * 80)