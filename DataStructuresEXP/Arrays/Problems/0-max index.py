length = int(input())
array = list(map(int, input().split(" ")))

max_index = 0

for i in range(1, length):
    if array[max_index] < array[i]:
        max_index = i 
        
print(max_index + 1)