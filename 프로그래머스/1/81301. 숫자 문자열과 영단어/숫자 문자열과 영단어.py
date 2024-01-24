def solution(s):
    Set = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four',
          5: 'five', 6: 'six', 7:'seven', 8:'eight', 9:'nine'}
    
    #print(Set[1])
    
    for i in Set:
        if Set[i] in s:
            s = s.replace(Set[i], str(i))
    #print(s)
    answer = int(s)
    return answer