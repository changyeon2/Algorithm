import math

numString = "0123456789"

def notationChange(n, k):
    # str -> O(logn)
    # list indexing -> O(1)
    
    q, r = divmod(n, k)
    
    return notationChange(q, k) + numString[r] if q else numString[r]

def primeTest(n, k):
    n = int(n)
    
    # 제곱근까지는 포함시켜야 정확한 소수 판별 가능!
    # -> 그냥 math.sqrt에 math.ceil만 하면, 제곱근 포함 안 되는 경우가 생긴다!
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    
    n = notationChange(n, k).split('0')
    
    for i in n:
        if i == '' or i == '1': continue
        
        if primeTest(i, k): answer += 1
    
    return answer
