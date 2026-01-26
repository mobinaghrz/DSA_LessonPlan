
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
    
    def insert(self, key, value):
        index = self.hash(key)
        self.map[index] = (key, value)

    def get(self, key):
        index = self.hash(key)
        slot = self.map[index]

        if slot is None or slot[0] != key:
            return
        
        return slot[1]
    
    def delete(self, key):
        """
        Input:
            - key: a string key identifying the entry to be removed

        Output:
            - None

        Description:
            This method removes a key-value pair from the hash map.

            The deletion process works as follows:
                - Compute the index using the hash function
                - Retrieve the slot at the computed index
                - If the slot is empty, the key does not exist
                - If the stored key does not match the provided key,
                deletion is aborted due to a hash collision
                - If the keys match, the slot is cleared by setting it to None

            This implementation does not support collision handling, so
            deletion is only reliable when no hash collisions occur.

        Time Complexity:
            - Average case: O(1)
            - Worst case:  O(1)

        Space Complexity:
            - O(1), constant extra space is used
        """
        index = self.hash(key)
        slot = self.map[index]

        if slot is None or slot[0] != key:
            return
        
        self.map[index] = None