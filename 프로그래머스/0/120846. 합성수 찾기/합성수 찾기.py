def solution(n):
    
    # 반복문을 통해서 자연수 n의 범위까지 약수를 찾기
    if n <= 3:
        return 0
    
    elif n >= 4:
        answer = 0 # 합성수의 개수
        for i in range(4, n + 1):
            num = []
            for j in range(1, i+1):
                if i % j == 0:
                    num.append(j)
                    if len(num) == 3:
                        answer += 1
                        
    # print(answer)
    return answer