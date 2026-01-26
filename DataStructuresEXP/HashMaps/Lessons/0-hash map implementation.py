class HashMap:
    """
    Input:
        - size: an integer representing the number of buckets in the hash map

    Output:
        - an initialized HashMap object with internal storage allocated

    Description:
        HashMap initializes a fixed-size array to be used as the underlying
        storage for a hash map data structure.

        During initialization:
            - The provided size is stored as an instance attribute
            - An internal list of length `size` is created
            - Each position in the list is initialized to None, representing
            an empty bucket

        This structure serves as the foundation for implementing hash map
        operations such as insertion, lookup, and deletion, which would rely
        on hashing keys to indices within this array.

    Time Complexity:
        - O(n), where n is the size of the hash map (due to list allocation)

    Space Complexity:
        - O(n), for the internal storage array
    """
    def __init__(self, size):
        self.size = size 
        self.map = [None] * size