def solution(s):
    #key = 'if you wanna christmas'
    A = []
    for i in s:
        A.append(i)
    print(A)
    
    count = 0
    for k in range(len(A)):
        if count % 2 == 0:
            A[k] = A[k].upper()
            if A[k] == " ":
                count = 0
                continue
        else:
            A[k] = A[k].lower()
            if A[k] == " ":
                count = 0
                continue
        count += 1
            
    print(A)
    
    answer = ''.join(A)
    return answer