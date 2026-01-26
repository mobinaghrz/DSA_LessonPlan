size = int(input())
array = list(map(int, input().split()))
target = int(input())


def solution(array, size, target, low=0, high=None):
    if high is None:
        high = size - 1

    if low > high:
        return -1
    
    mid = (low + high) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return solution(array, size, target, low, mid - 1)
    else:
        return solution(array, size, target, mid+1, high)
    

print(solution(array, size, target))