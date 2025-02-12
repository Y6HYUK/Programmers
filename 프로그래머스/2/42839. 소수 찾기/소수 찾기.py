from itertools import permutations
def solution(numbers):
    
    # numbers의 조합을 통해 만들 수 있는 숫자를 저장할 리스트 
    answer = []
    
    # numbers의 길이를 n 으로 설정하고
    # 1자리부터 n자리 까지 모든 순열 permutations을 생성
    for i in range(1, len(numbers) + 1):
        # permutations(number, i) 는 numbers의 문자들을 i개씩 (i자리수) 뽑은 순열을 생성함
        for j in permutations(numbers, i):
            # ex) numbers 가 "17"이면 i = 1일때 ('1'), ('7')
            # i = 2일때, ('1', '7'), ('7', '1')가 생성됨
            # 생성된 튜플을 ''.join(j)로 문자열을 만들고, int로 숫자로 변형
            num = int(''.join(j))
            answer.append(num)
            
    # 소수 판별 알고리즘
    def is_prime(n):
        if n < 2 : # 0, 1은 소수가 아님
            return False
            
        else: 
            # n의 제곱근까지만 검사
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False # 나머지가 0이면 소수가 아님

        return True
                
    # answer의 중복 삭제
    answer = list(set(answer))
    print(answer)
    
    count = 0
    for k in answer:
        if is_prime(k):
            count += 1
    
    return count