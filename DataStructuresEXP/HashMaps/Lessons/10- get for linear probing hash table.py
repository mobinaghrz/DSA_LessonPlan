
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

    def get(self, key):
        """
        Input:
            - key: a string key identifying the entry to be retrieved

        Output:
            - The value associated with the provided key if found
            - None if the key is not present in the hash map

        Description:
            This method retrieves the value associated with the provided key from the hash map
            using linear probing (open addressing) to handle collisions.

            The lookup process works as follows:
                - Compute the initial bucket index using the hash function
                - Inspect the slot at the computed index:
                    - If the slot is empty (None), the key is not in the table and None is returned
                    - If the slot contains a pair whose key matches the provided key, return its value
                    - Otherwise, advance to the next slot (index + 1) and continue probing,
                    wrapping around to index 0 when reaching the end of the array
                - If probing returns to the original index, the entire table has been scanned
                and the key was not found, so None is returned

            This implementation resolves collisions via open addressing with linear probing,
            so keys may be stored at positions different from their original hash index.

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
                return self.map[index][1]

            index = (index + 1) % self.size
            if index == initial_index:
                return 