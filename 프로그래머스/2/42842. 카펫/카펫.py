def solution(brown, yellow):
    # 공식 계산하기
    # brown x yellow = return
    # return 의 약수를 뽑아내서, 가로길이 = 세로길이 / 가로길이 > 세로길이 인 것을 return
    
    mul_caffet = brown + yellow
    
    answer = []
    # 1부터 mul_caffet의 반이 되는 지점까지 순회하며 약수 저장
    for i in range(1, mul_caffet // 2 + 1):
        if mul_caffet % i == 0: # 약수의 짝을 저장하기 위함
            j = mul_caffet // i 
            if i >= j and j != 2: # 세로길이가 2이면 안됨
                pre_answer = [i, j]
                answer.append(pre_answer) # 약수의 짝을 리스트에 저장
                
    for j in answer:
        if yellow % 2 == 0:
            if (j[0] - 2) * (j[1] - 2) == yellow:
                return j
        else:
            return j
            
    print(answer)