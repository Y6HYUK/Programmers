def solution(s):
    A = [-1] # 맨 처음 나오는 값 Default : -1
    B = [] # 그 이후에 이어지는 단어들을 저장하기 위한 리스트
    for i in range(1,len(s)):
        B.append(s[i-1])
        #print(B)
        
        if s[i] not in B:
            A.append(-1)
        else:
            if B.count(s[i]) > 1: # 앞에 중복되는 단어가 2개 이상이면
                # rindex를 사용하기 위해 리스트B를 문자열로 변환
                New_B = ''.join(B)
                A.append(i-New_B.rindex(s[i]))
            else:
                A.append(i-B.index(s[i]))
          
    #print(A)        
        
    answer = A
    return answer