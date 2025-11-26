n, i = map(int, input().split(" "))
array = list(map(int, input().split(" ")))


def array_to_sequence(array):
    return " ".join(map(str, array))

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def solution(array, size, level):
    counter = 0
    
    if size in [0, 1]:
        print(array_to_sequence(array))
        return
    
    for i in range(1, size):
        j = i
        
        while j != 0 and array[j] < array[j-1]:
            swap(array, j, j - 1)
            j -= 1
            
        
        counter += 1
        
        if counter == level:
            print(array_to_sequence(array))
            break
        
solution(array, n, i)