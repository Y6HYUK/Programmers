def solution(n):
    if n**0.5 == int(n**0.5):
        answer = ((n**0.5)+1)*((n**0.5)+1)
    else:
        answer = -1
    return answer