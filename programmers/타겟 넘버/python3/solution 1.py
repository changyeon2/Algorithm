# DFS라는게 graph에 국한되는 것이 아니라, 한방향 쭉 파본다음에 갈림길로 돌아와서 탐색을 재개하는, 이런 재귀 알고리즘도 다 포함하는 개념임!

def DFS(numbers, target, curSum, curIdx):
    if curIdx == len(numbers):
        if curSum == target:
            return 1
        else:
            return 0
    
    return DFS(numbers, target, curSum + numbers[curIdx], curIdx+1) \
            + DFS(numbers, target, curSum - numbers[curIdx], curIdx+1)


def solution(numbers, target):
    return DFS(numbers, target, +numbers[0], 1) + DFS(numbers, target, -numbers[0], 1)
    
