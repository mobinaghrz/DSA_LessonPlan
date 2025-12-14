n, q = map(int, input().split())

def solution(n, q):
    front = [0] * n
    pref = [0]

    for _ in range(q):
        parts = input().split()
        if parts[0] == "1":
            x = int(parts[1])
            pref.append(pref[-1] + x)
        else:
            i = int(parts[1])
            j = int(parts[2])

            s = front[i]
            e = s + j

            print(pref[e] - pref[s])
            front[i] = e

solution(n, q)