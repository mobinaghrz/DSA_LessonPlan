def min_and_max_pairwise(array):
    """
        Input:
            - an array of n elements

        Output:
            - a tuple of two element. 
              first value is minimum value.
              second value is maximum value.

        Comparisons: 3 * seil(n/2) - 2

        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    n = len(array)

    if n < 2:
        raise Exception("array must have at least 2 elements")
    
    i = 0
    mins = []
    maxs = []

    # pairing elements and separating them into two lists
    while i + 1 < n:
        if array[i] < array[i+1]:
            mins.append(array[i])
            maxs.append(array[i+1])
        else:
            mins.append(array[i+1])
            maxs.append(array[i])
        
        i += 2

    # handle the odd amount of elements for array
    if i < n:
        mins.append(array[i])
        maxs.append(array[i])

    
    # find the minimum value
    minimum = mins[0]
    for value in mins:
        if value < minimum:
            minimum = value

    #find the maximum value
    maximum = maxs[0]
    for value in maxs:
        if value > maximum:
            maximum = value

    return minimum, maximum
    

def min_and_max(array):
    """
        Input:
            - an array of n elements

        Output:
            - a tuple of two element. 
              first value is minimum value.
              second value is maximum value.

        Comparisons: 2 * (n - 1)

        Time Complexity: O(n)
        Space Complexity: O(1)
    """

    n = len(array)

    if n <= 2:
        raise Exception("array must have at least 2 elements")


    minimum = array[0]
    maximum = array[1]

    for value in array[2:]:
        if value < minimum:
            minimum = value

        if value > maximum:
            maximum = value

    return minimum, maximum