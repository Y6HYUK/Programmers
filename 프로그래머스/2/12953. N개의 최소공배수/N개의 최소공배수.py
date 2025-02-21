# 최소공배수 함수 사용하기
# 최소공배수 함수 : lcm
# 최대공약수 함수 : gcd
import math
# lcm을 사용할 수 없다고 나오므로, gcd를 사용하여 lcm 함수를 생성해주기
def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(arr):
    answer = 1
    for num in arr:
        answer = lcm(answer, num)
    return answer
