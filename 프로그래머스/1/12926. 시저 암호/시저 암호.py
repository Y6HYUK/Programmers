def solution(s, n):
    Lo = 'abcdefghijklmnopqrstuvwxyz'
    Up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    result = []
    
    for i in s:
        for j in range(len(Lo)):
            if i == Lo[j]:
                #result.append(i)
                NEW = Lo.index(i) + n
                if 0 <= NEW < len(Lo):
                    result.append(Lo[NEW])
                else:
                    result.append(Lo[NEW - len(Lo)])
                
            elif i == Up[j]:
                #result.append(i)
                NEW = Up.index(i) + n
                if 0 <= NEW < len(Up):
                    result.append(Up[NEW])
                else:
                    result.append(Up[NEW - len(Up)])
                
            elif i == ' ':
                result.append(i)
                break
            
    
    answer = ''.join(result)
    return answer