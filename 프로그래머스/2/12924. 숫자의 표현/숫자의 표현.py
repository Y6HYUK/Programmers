def solution(n):
    count = 0 # 연속된 숫자가 합이 n이 되는 횟수
    
    for i in range(1, n+1):
        answer = 0
        for j in range(i, n+1):
            answer += j
            if answer == n:
                count += 1
                break
                
            elif answer > n:
                break
                
    # print(count)
        # print(answer)
    return count