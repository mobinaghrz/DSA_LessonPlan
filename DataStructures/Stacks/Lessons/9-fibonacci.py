def fibonacci(n):
    """
    Input:
        - n (int): A non-negative integer representing the position in the
          Fibonacci sequence.

    Output:
        - int:
            - The Fibonacci number corresponding to position n.

    Description:
        The fibonacci function computes the nth Fibonacci number using
        a recursive approach.

        Base Cases:
            - If n is 0 or 1:
                - Return 1.

        Recursive Case:
            - For n > 1:
                - The function returns the sum of the two preceding
                  Fibonacci numbers:
                    fibonacci(n - 1) + fibonacci(n - 2)

        Process:
            - Step 1: Check if n is a base case:
                - If n is 0 or 1:
                    - Immediately return 1.

            - Step 2: Apply the recursive formula:
                - Call fibonacci(n - 1)
                - Call fibonacci(n - 2)
                - Return their sum.

        Invariants relied upon:
            - n is assumed to be a non-negative integer.
            - The function follows the recursive definition of the
              Fibonacci sequence.
            - Each recursive call reduces the value of n, ensuring
              eventual termination at a base case.

    Time Complexity:
        - O(2^n), due to repeated recalculation of overlapping
          subproblems in the naive recursive approach.

    Space Complexity:
        - O(n), due to the recursion call stack depth.
    """
    if n in [0, 1]:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)
