
def minimal_period(arr):
    m = len(arr)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and arr[i] != arr[j]:
            j = pi[j - 1]
        if arr[i] == arr[j]:
            j += 1
            pi[i] = j
    return m - pi[-1] 

def solution():
    t = int(input())
    out_lines = []

    for _ in range(t):
        m = int(int(input())) 
        b = list(map(int, input().split()))

        p = minimal_period(b)
        a = b[:p]

        out_lines.append(str(p))
        out_lines.append(" ".join(map(str, a)))

    print("\n".join(out_lines))

solution()