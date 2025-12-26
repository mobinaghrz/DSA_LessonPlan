def fibonacci(n):
    """
    Input:
        - n (int): An integer greater than or equal to 2 representing
          the position in the Fibonacci sequence.

    Output:
        - tuple (int, int):
            - A tuple containing:
                - The nth Fibonacci number.
                - The (n-1)th Fibonacci number.

    Description:
        The fibonacci function computes Fibonacci numbers using a
        recursive approach that returns a pair of consecutive values.

        Specifically, the function returns:
            (F(n), F(n-1))

        instead of computing only a single Fibonacci number. This avoids
        redundant recursive calls and improves efficiency compared to
        the naive recursive Fibonacci implementation.

        Base Case:
            - If n == 2:
                - Return the tuple (1, 1), representing:
                    F(2) = 1
                    F(1) = 1

        Recursive Case:
            - Call fibonacci(n - 1) to obtain a tuple:
                u = (F(n-1), F(n-2))
            - Compute the result tuple as:
                (u[0] + u[1], u[0])
              which corresponds to:
                (F(n), F(n-1))

        Process:
            - Step 1: Check for the base case:
                - If n == 2:
                    - Return (1, 1).

            - Step 2: Recursive computation:
                - Recursively call fibonacci(n - 1).
                - Store the returned tuple in variable `u`.

            - Step 3: Construct the result:
                - Compute F(n) as u[0] + u[1].
                - Use u[0] as F(n-1).
                - Return the tuple (u[0] + u[1], u[0]).

        Invariants relied upon:
            - n is assumed to be an integer greater than or equal to 2.
            - Each recursive call reduces n by 1.
            - The returned tuple always follows the structure:
                (F(k), F(k-1)).
            - The recursion terminates at the base case n == 2.

    Time Complexity:
        - O(n), as the function makes exactly one recursive call per level.

    Space Complexity:
        - O(n), due to the recursion call stack depth.
    """
    if n == 2:
        return (1, 1)
    
    u = fibonacci(n-1)
    return (u[0] + u[1], u[0])