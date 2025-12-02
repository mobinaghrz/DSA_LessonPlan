def max_index(array):
    """
        Input: 
            - an array of n elements

        Output:
            -  index of maximum value in the array
    
        Time Complexity: O(n)
        Space Complexity: O(1)
    """

    max_index = 0

    for i in range(1, len(array)):
        if array[i] > array[max_index]:
            max_index = i

    return max_index