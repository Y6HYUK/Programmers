def solution(s):
    stack = []
    
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    print(stack)
    
    if len(stack) == 0:
        return 1
    else:
        return 0
    
#     for i in s:
#         if i not in stack:
#             stack.append(i)
#         else:
#             if i == stack[-1]:
#                 stack.pop()
                
#     if len(stack) == 0:
#         return 1
#     else:
#         return 0
            
        
        