# main idea : 수열을 만들 수 있는 경우는 2*N(goalIndex(N)+numsIndex(N))만큼 iteration을 진행했을 때! 
# 불가능한 경우는 goalIndex는 증가하지 않고, numsIndex가 N보다 커지는 경우 (이거를 이용해서 isPossible flag 설정!)

import sys

from queue import LifoQueue

stack = LifoQueue()

result = []

nums = []
goalSeq = []

numsIndex = 0
goalIndex = 0

N = int(sys.stdin.readline().strip())

isPossible = True

for i in range(N):
    nums += [i+1]
    goalSeq += [int(sys.stdin.readline().strip())]

while True:
    if goalIndex == N and numsIndex == N:
        break
    elif numsIndex > N:
        isPossible = False
        break

    if stack.empty():
        if numsIndex < N:
            stack.put(nums[numsIndex])
        result += ["+\n"]
        numsIndex += 1
    
    else:
        topOfStack = stack.get()

        if topOfStack == goalSeq[goalIndex]:
            result += ["-\n"]
            goalIndex += 1
        
        else:
            stack.put(topOfStack)
            if numsIndex < N:
                stack.put(nums[numsIndex])
            result += ["+\n"]     
            numsIndex += 1

if isPossible:
    [sys.stdout.write(x) for x in result]
else:
    sys.stdout.write("NO\n")
