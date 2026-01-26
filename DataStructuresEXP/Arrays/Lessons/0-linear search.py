def linear_search(array, target):
    """
        Input:
            - an array of n elements
            - the element to search for

        Output:
            - index of target if found, or -1 if not found

        Time Complexity: O(n)
        Space Complexity: O(1)
    """

    for i in range(len(array)):
        if array[i] == target:
            return i
        
        return -1