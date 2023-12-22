def solution(arr):
    if len(arr) > 2:
        arr.remove(min(arr))
        answer = arr
    else:
        answer = [-1]
    
    return answer