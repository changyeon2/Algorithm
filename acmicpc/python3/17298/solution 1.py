# 알게된 사실 : 1. string = string + "something" 하면 새로운 배열을 계속해서 할당함! -> 타임아웃 가능성 있음
#           : 2. deque는 append, pop이 O(1), list는 append는 amortized O(1), pop은 O(1)임. getItem 연산을 주로 생각하면 list가 좋을 듯? middle에 접근하는 경우 list는 O(1)인데, deque는 O(n)이므로! 
#               (위 2번은 알고리즘 분석법 좀 더 공부하고 더 찾아볼 것!(
# main idea : 입력받은 순서의 반대로 수들을 탐색하면서, ngeStack에 nge가 없으면 result에는 -1를, ngeStack에는 그 수를 넣고,
#             있으면 result에 ngeStack[-1] (topOfStack)을 넣고, ngeStack에 그 수를 넣음!

import sys

sizeOfSeq = int(sys.stdin.readline().rstrip())

numStack = [int(x) for x in sys.stdin.readline().split()]

ngeStack = deque()

result = deque()

for i in range(sizeOfSeq-1, -1, -1):
    while ngeStack and ngeStack[-1] <= numStack[i]:
        ngeStack.pop()

    if not(ngeStack):
        result.append(-1)
    else:
        result.append(ngeStack[-1])
    
    ngeStack.append(numStack[i])

for i in range(sizeOfSeq):
    if i == (sizeOfSeq - 1):
        sys.stdout.write(str(result.pop()) + "\n")
    else:
        sys.stdout.write(str(result.pop()) + " ")
