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
    
    
def insertion_sort(array):
    """
    Input:
        - array: a list of n comparable elements

    Output:
        - the same array sorted in non-decreasing order (ascending)

    Description:
        Insertion Sort builds the final sorted array one element at a time.
        
        The algorithm starts from the second element (index 1), treating the 
        first element as a sorted subarray of size 1.

        For each element at index i:
            - Store its position in j
            - Compare array[j] with array[j - 1]
            - While it is smaller than its predecessor, swap them and move j 
              one step left
            - Continue until the correct position for the element is found 
              (or j reaches 0)
        
        This effectively inserts each element into its correct position in the 
        already sorted left portion of the array.

    Time Complexity:
        - Worst case: O(n^2)
        - Best case:  O(n) when the array is already sorted

    Space Complexity:
        - O(1), since sorting is done in-place
    """
    
    if len(array) in [0, 1]:
        return array
    
    for i in range(1, len(array)):
        j = i
        
        while j != 0 and array[j] < array[j-1]:
            swap(array, j, j - 1)
            
    return array