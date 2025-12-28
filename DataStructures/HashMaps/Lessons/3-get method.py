
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
        """
        Input:
            - key: a string key whose associated value is to be retrieved

        Output:
            - the value associated with the key if found
            - None if the key is not present in the hash map

        Description:
            This method retrieves the value associated with a given key
            from the hash map.

            The lookup process works as follows:
                - Compute the index using the hash function
                - Access the storage slot at the computed index
                - If the slot is empty, the key does not exist
                - If the slot contains a key different from the requested key,
                the lookup fails due to a hash collision
                - If the keys match, return the corresponding value

            Because this implementation does not support collision handling,
            retrieval is only guaranteed to work correctly when no collisions
            occur in the hash map.

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
        
        return slot[1]