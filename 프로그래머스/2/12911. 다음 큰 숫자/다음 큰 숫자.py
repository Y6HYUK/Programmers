def solution(n):
    
    bin_n = bin(n)[2:] # 2진수로 변환
    count_bin_n = bin_n.count('1') # 2진수에서 1의 개수 찾기
    
    next_n = n+1 # n의 다음 자연수부터 확인을 해야함
    
    while True:
        bin_next_n = bin(next_n)[2:] # n 다음 자연수의 2진수
        count_next_n = bin_next_n.count('1') # n 다음 2진수에서 1의 개수
        
        # 만약 count_bin_n 과 count_next_n이 같다면 그 값이 n 다음 큰 숫자이다.
        if count_bin_n == count_next_n:
            answer = int(bin(next_n), 2)
            break
            
        next_n += 1 # 만약 1의 개수가 같지 않다면, 1씩 증가시키면서 순회하기
    
    
    print(answer)
    
    return answer