# main idea : stack이 empty인데 넓이 구하는 상황이면, 그 index까지 그 친구가 가장 작은 애라는 것이므로 그냥 width = i가 됨!
#             empty가 아니면 left가 존재하는 것으로, (right - left - 1) 한 값을 width로 쓰면 됨!
#             stack 활용 idea - 왼쪽에서 오른쪽으로 탐색을 하는데, 보고자하는 인덱스의 높이가 topOfStack보다 작은 경우, 더이상 직사각형을 연장할 수 없으므로 pop해서 넓이 구함!!
#                              결국 하고자 하는 것은 각 인덱스의 직사각형을 양옆으로 연장 가능할 때까지(유효할 때까지) 늘린다음 그 넓이를 구하는데, 이중에서 최대를 찾겠다는 뜻!

import sys
from collections import deque

histLen = int(sys.stdin.readline().rstrip())
histHeights = dict()

stack = deque()

biggestRect = 0

[histHeights.update({i : int(sys.stdin.readline().rstrip())}) for i in range(histLen)]

for i in range(histLen):
    while stack and histHeights[stack[-1]] > histHeights[i]:
        width = i
        height = histHeights[stack.pop()]

        # left와 right 사이의 간격을 구함(i - stack[-1]), 그리고 한 칸 더 간 right을 빼줌(-1)!
        if stack:
            width = i - stack[-1] - 1
        
        biggestRect = max(biggestRect, width*height)

    stack.append(i)

while stack:
    width = histLen
    height = histHeights[stack.pop()]

    if stack:
        width = histLen - stack[-1] - 1
    
    biggestRect = max(biggestRect, width*height)

sys.stdout.write(str(biggestRect) + '\n')


