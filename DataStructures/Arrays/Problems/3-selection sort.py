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
    
    for i in range(size):
        min_index = i
        
        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j 
                
        if i != min_index:
            swap(array, i, min_index)
            
        if i + 1 == level:
            print(array_to_sequence(array))
            return
        
solution(array, n, i)