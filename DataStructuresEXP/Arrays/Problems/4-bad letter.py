letter = input()

def solution(letter):
    size = len(letter)
    
    if size == 1:
        print("bad")
        return
    
    char_frequency = 1
    for i in range(1, size):
        if letter[i] == letter[i-1]:
            char_frequency += 1 
        else:
            if char_frequency % 2 == 1:
                print("bad")
                return
            else:
                char_frequency = 1 
                
    if char_frequency % 2 == 1:
        print("bad")
    else:
        print("khoob")

solution(letter)