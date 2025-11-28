def swap(array, i, j):
    """
        Input:
            - an array of n elements
            - index one
            - index two
        Output:
            - void
            
        Description:
            Swap elements of two indicies
            
        Time Complexity: 
            - O(1)
            
        Space Complexity:
            - O(1)
    """
    array[i], array[j] = array[j], array[i]

def bubble_sort(array):
    """
    Input:
        - array: a list of n comparable elements

    Output:
        - the same list sorted in non-decreasing (ascending) order

    Description:
        Bubble Sort repeatedly steps through the array, comparing adjacent 
        elements and swapping them if they are in the wrong order.

        The algorithm works in passes:
            - On each pass, the largest unsorted element "bubbles up" to its 
              correct position at the end of the list.
            - After the i-th pass, the last i elements are guaranteed to be 
              sorted, so the inner loop becomes shorter each time.

        For each pass i:
            - Compare array[j] with array[j + 1]
            - Swap if array[j] > array[j + 1]

        The process repeats until the entire array is sorted.

    Time Complexity:
        - Worst case: O(n^2)
        - Best case:  O(n) with optimized version (not implemented here)
        - Average:    O(n^2)

    Space Complexity:
        - O(1), sorting is done in-place
    """
    size = len(array)
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)
    
    return array