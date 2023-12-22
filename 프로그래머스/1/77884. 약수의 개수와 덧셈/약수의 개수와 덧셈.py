def solution(left, right):
    LtoR = []
    for i in range(left, right + 1):
        LtoR.append(i)
    
    A = [] # 약수의 개수 파악하기 위한 빈 리스트    
    for j in LtoR:
        B = [] # 해당 j 숫자에 대한 약수 개수를 알기 위한 빈 리스트
        for k in range(1,j+1):
            if j % k == 0:
                B.append(k)
                
        A.append(len(B)) # 다시 for문이 시작하기 전에 리스트 A에 약수의 개수 추가.
                
    for i in range(len(LtoR)):
        if A[i] % 2 != 0:
            LtoR[i] = -LtoR[i]
    
    answer = sum(LtoR)
    return answer