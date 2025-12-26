size = int(input())
elements = list(map(int, input().split(" ")))

def solution(size, elements):
    max_area = 0
    indicies_stack = []

   
    elements.append(0)

    for i, v in enumerate(elements):
        while indicies_stack and elements[indicies_stack[-1]] > v:
            top_index = indicies_stack.pop()
            height = elements[top_index]

            if not indicies_stack:
                width = i
            else:
                width = i - indicies_stack[-1] - 1

            area = height * width
            if area > max_area:
                max_area = area

        indicies_stack.append(i)

    elements.pop()
    print(max_area)

solution(size, elements)
