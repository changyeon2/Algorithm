# main idea : 한 건물'이' 관찰가능한 건물 수를 더하는 것이 아닌, 한 건물'을' 관찰가능한 건물 수를 더하는 것으로 관점을 바꿈!
#             첫 건물부터 돌면서 stack에 그 건물보다 큰 건물만 있도록 한 뒤에(물론 인덱스는 이 건물보다 작은 애들만 있음) 그 스택의 길이가 곧,
#             그 건물을 관찰가능한 건물의 수가 되므로 이를 visibleRoofTopCount에 더함!!

import sys

from collections import deque

buldNum = int(sys.stdin.readline().rstrip())
buldHeightDict = dict()

visibleRoofTopCount = 0

stack = deque(maxlen=buldNum)

for i in range(buldNum):
    buldHeightDict[i] = int(sys.stdin.readline().rstrip())

for i in range(buldNum):
    while(stack and buldHeightDict[i] >= stack[-1]):
        stack.pop()

    visibleRoofTopCount += len(stack)

    stack.append(buldHeightDict[i])

sys.stdout.write(str(visibleRoofTopCount) + '\n')
