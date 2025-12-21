size = int(input())
elements = list(map(int, input().split(" ")))

def solution(size, elements):
    answer = [-1] * size
    indicies_stack = []

    for i, v in enumerate(elements):
        while indicies_stack and elements[indicies_stack[-1]] < v:
            index = indicies_stack.pop()
            answer[index] = v

        indicies_stack.append(i)

    print(*answer)

solution(size, elements)