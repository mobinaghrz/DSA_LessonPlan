def binary_search(array, target, low=0, high=None):
    """
    Input:
        - array (list): A sorted list of comparable elements.
        - target: The value to search for in the array.
        - low (int, optional): The lower bound index of the search range.
        - high (int, optional): The upper bound index of the search range.

    Output:
        - int:
            - The index of the target element if found.
            - Returns -1 if the target is not present in the array.

    Description:
        The binary_search function performs a recursive binary search
        on a sorted array to locate a target value.

        The search space is repeatedly divided in half by comparing
        the target value with the middle element of the current range.

        Process:
            - Step 1: Initialize search boundaries:
                - If high is None:
                    - Set high to len(array) - 1.

            - Step 2: Check termination condition:
                - If low > high:
                    - The target is not in the array.
                    - Return -1.

            - Step 3: Compute the middle index:
                - mid = (low + high) // 2

            - Step 4: Compare the middle element with the target:
                - If array[mid] == target:
                    - Return mid.
                - If array[mid] > target:
                    - Recursively search the left subarray:
                        low to mid - 1.
                - Otherwise:
                    - Recursively search the right subarray:
                        mid + 1 to high.

        Invariants relied upon:
            - The input array is sorted in ascending order.
            - low and high define a valid search interval.
            - Each recursive call reduces the size of the search range.
            - The algorithm follows the divide-and-conquer paradigm.

    Time Complexity:
        - O(log n), where n is the number of elements in the array.

    Space Complexity:
        - O(log n), due to recursive call stack usage.
    """
    if high is None:
        high = len(array) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, low, mid - 1)
    else:
        return binary_search(array, target, mid + 1, high)
    