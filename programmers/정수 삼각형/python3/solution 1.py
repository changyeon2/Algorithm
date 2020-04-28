# 그냥 copy하면 내부 element로 list가 있을 때, 걔네는 같은 주소를 그대로 가지고 간다는 문제 발생!
# 따라서 내부 element가 정수 같은 immutable한 타입이면 그냥 copy(shallow copy, 큰 껍데기만 새걸로 채우는 것)해도 되지만, mutable 타입일 경우 deepcopy를 해줘야 함!

from copy import deepcopy

def solution(triangle):
    memo = deepcopy(triangle)
    
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            leftIdx = j
            rightIdx = j + 1
            
            memo[i][j] += max(memo[i+1][leftIdx], memo[i+1][rightIdx])
            
    return memo[0][0]
            
            
