
class HashMap:
    def __init__(self, size):
        self.size = size 
        self.map = [None] * size

    def hash(self, key):
        """
        Input:
            - key: a string key whose characters are used to compute a hash value

        Output:
            - an integer index within the bounds of the hash map's storage array

        Description:
            This method computes a hash index for a given key using a simple
            character-sum hashing technique.

            The hashing process works as follows:
                - Initialize a hash code accumulator to zero
                - Iterate through each character in the key
                - Convert the character to its Unicode code point using ord()
                - Add this value to the running hash code
                - After processing all characters, apply modulo operation
                with the hash map size to ensure the index fits within bounds

            The resulting index corresponds to a bucket in the internal
            storage array where the key-value pair can be stored.

            This hash function is simple and easy to understand but may
            produce collisions for different keys with the same character sum.

        Time Complexity:
            - O(k), where k is the length of the key

        Space Complexity:
            - O(1), constant extra space is used
        """
        hash_code = 0
        for char in key:
            hash_code += ord(char)

        index = hash_code % self.size 
        return index