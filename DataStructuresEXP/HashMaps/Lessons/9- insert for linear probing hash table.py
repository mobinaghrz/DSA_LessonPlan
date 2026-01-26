
class HashMap:
    def __init__(self, size):
        self.size = size 
        self.map = [None] * size

    def hash(self, key):
        hash_code = 0
        for char in key:
            hash_code += ord(char)

        index = hash_code % self.size 
        return index
    
    def insert(self,key, value):
        """
        Input:
            - key: a string key identifying the entry to be inserted/updated
            - value: the value to be associated with the provided key

        Output:
            - None

        Description:
            This method inserts a key-value pair into the hash map using linear probing
            to resolve collisions.

            The insertion process works as follows:
                - Compute the initial bucket index using the hash function
                - If the computed slot is empty (None), store the (key, value) pair there
                - If the slot is occupied:
                    - If the stored key matches the provided key, update the existing
                    entry by replacing it with the new (key, value) pair
                    - Otherwise, advance to the next slot (index + 1) and continue probing,
                    wrapping around to index 0 when reaching the end of the array
                - If probing returns to the original index, the table is full and an
                exception is raised

            This implementation handles hash collisions via open addressing with linear
            probing, so all entries are stored directly in the underlying array.

        Time Complexity:
            - Average case: O(1) expected (assuming uniform hashing and a reasonable load factor)
            - Worst case:  O(n) where n is the size of the table (when many slots are occupied)

        Space Complexity:
            - O(1), constant extra space is used per operation
        """
        index = self.hash(key)
        initial_index = index 

        while self.map[index] is not None:
            if self.map[index][0] == key:
                self.map[index] = (key, value)
                return 
            
            index = (index + 1) % self.size
            if index == initial_index:
                raise Exception("hash table is full")
            
        self.map[index] = (key, value)