def solution(s):
    num_list = s.split(' ') # split 메서드를 사용하여 공백을 기준으로 문자열 나누기
    print(num_list)
    
    answer = []
    for i in num_list:
        i = int(i)
        answer.append(i)
    
    max_num = str(max(answer))
    min_num = str(min(answer))
    
    return min_num +' '+ max_num
    