
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
        """
        Input:
            - key: a hashable string used to determine the storage index
            - value: the data associated with the key

        Output:
            - None

        Description:
            This method inserts a key-value pair into the hash map using
            direct addressing based on the computed hash index.

            The insertion process works as follows:
                - Compute the index by applying the hash function to the key
                - Store the (key, value) tuple at the computed index in the
                internal storage array

            This implementation does not handle collisions. If multiple keys
            hash to the same index, the newly inserted key-value pair will
            overwrite the existing entry at that position.

            This approach represents the simplest form of a hash map and
            serves as a foundation for more advanced implementations that
            support collision resolution techniques such as chaining or
            open addressing.

        Time Complexity:
            - Average case: O(1)
            - Worst case:  O(1) (no collision handling logic)

        Space Complexity:
            - O(1), constant extra space per insertion
        """
        index = self.hash(key)
        self.map[index] = (key, value)