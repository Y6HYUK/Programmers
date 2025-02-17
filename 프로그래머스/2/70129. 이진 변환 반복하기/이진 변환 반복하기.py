def solution(s):
    count1 = 0 # 제거할 0의 수
    count2 = 0 # 회차
    while True:
        zero_count = s.count('0')
        count1 += zero_count
        count2 += 1 
        new_s = s.replace('0','')
        len_s = len(new_s)
        
        s = format(len_s, 'b')
        
        if s == '1':
            return count2, count1
        