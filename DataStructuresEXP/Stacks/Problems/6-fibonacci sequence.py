def solution(n):
    if n == 0:
        return (0, 0)
    if n == 1:
        return (1, 0)

    a, b = solution(n - 1)
    return (a + b, a)


n = int(input())
print(solution(n)[0])