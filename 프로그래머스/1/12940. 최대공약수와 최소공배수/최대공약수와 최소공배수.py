def solution(n, m):
    if m % n == 0:
        a = n
        b = m
        answer = [a,b]
    else:
        A = [] # n의 약수를 알아보기 위한 빈 리스트
        B = [] # 최대 공약수 를 알아보기 위한 빈 리스트
        for i in range(1,n+1):
            if n % i == 0:
                A.append(i) # 입력값 n의 약수를 리스트 A에 추가
                
        for j in A:
            if m % j == 0: 
                B.append(j) # n의 약수 중에 m의 약수가 되는 숫자 찾기
                
        a = max(B) # 최대 공약수는 공통 약수중 최대 값임
        c = int(n/a)
        d = int(m/a)
        b = a*c*d
        
        answer = [a,b]
    
    return answer
