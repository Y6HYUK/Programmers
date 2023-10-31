def solution(n):
    A = list(str(n))
    B = []
    for i in A:
        B.append(int(i))
    B.sort(reverse = True)
    
    resurt = int(''.join(map(str,B)))
    
    return resurt
    
