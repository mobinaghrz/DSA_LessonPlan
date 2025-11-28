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

def selection_sort(array):
    """
    Input:
        - array: a list of n comparable elements

    Output:
        - the same list sorted in non-decreasing (ascending) order

    Description:
        Selection Sort organizes the array by repeatedly selecting the smallest
        element from the unsorted portion and placing it at the correct sorted
        position.

        The algorithm divides the array into two regions:
            - a sorted region at the beginning
            - an unsorted region for the remainder of the array

        For each position i:
            - Assume the smallest value is at index i (min_index = i)
            - Compare this assumed minimum with every element in the unsorted
              portion (from i+1 to the end)
            - If a smaller element is found, update min_index to that position
            - After scanning the unsorted portion, swap the element at i with
              the smallest element found (at min_index)

        After each iteration:
            - The element at position i is guaranteed to be the correct value
              for that position in the sorted order

        This process continues until the entire array becomes sorted.

    Time Complexity:
        - Worst case: O(n^2)
        - Best case:  O(n^2)    (still must search full unsorted region)
        - Average:    O(n^2)

    Space Complexity:
        - O(1), sorting is performed in-place
    """
    size = len(array)
    
    for i in range(size):
        min_index = i 
    
        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j
                
        if i != min_index:
            swap(array, i, min_index)

    return array
