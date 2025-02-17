def solution(s):
    if s[0] == ')' or s[-1] == '(':
        return False
    
    else:
        count_open = 0
        count_close = 0
        if len(s) % 2 == 0:
            for i in s:
                if i == '(':
                    count_open += 1
                else:
                    count_close += 1

                if count_close > count_open:
                    return False
            if count_close != count_open:
                return False
            else:
                return True
                
            # return True #위의 조건이 성립하지 않으면 올바른 괄호임
    
        else:
            return False # 문자열 s의 길이가 홀수라면 성립하지 않음
            
    
    
    
#     if s[0] == ')' or s[-1] == '(':
#         return False
        
#     else:
#         count_open = s.count('(')
#         count_close = s.count(')')
        
#         if count_open == count_close:
#             return True
            
#         else:
#             return False