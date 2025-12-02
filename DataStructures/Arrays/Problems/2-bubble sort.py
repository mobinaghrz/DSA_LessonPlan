n, i = map(int, input().split(" "))
array = list(map(int, input().split(" ")))

def array_to_sequence(array):
    return " ".join(map(str, array))

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    
def solution(array, size, level):    
    if size in [0, 1]:
        print(array_to_sequence(array))
        return
    
    for step in range(size - 1):
        for j in range(size - 1 - step):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)
                
        if step+1 == level:
            print(array_to_sequence(array))
            return
        
        
    print(array_to_sequence(array))
    
solution(array, i)