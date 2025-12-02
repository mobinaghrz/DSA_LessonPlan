def min_index(array):
    """
        Input:
            - an array of n elements
        
        Output:
            - index of minimum value in the array

        Time Complexity: O(n)
        Space Complexity: O(1)
    """

    min_index = 0
    for i in range(1, len(array)):
        if array[i] < array[min_index]:
            min_index = i
    
    return min_index