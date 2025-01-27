def solution(numbers, k):
    
    if len(numbers) % 2 == 0:
        index = ((2*k - 1) - 1) % len(numbers)
        answer = numbers[index]
        return answer
    
    else:
        index = ((2*k - 1) - 1) % len(numbers)
        answer = numbers[index]
        return answer