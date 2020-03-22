# main idea : TopOfStack 확인해보면서 매칭하는 거 있으면 빼고, 아니면 넣음! 마지막에 empty가 True면 좋은 단어인 것

import sys

from queue import LifoQueue

result = 0

wordsNum = int(sys.stdin.readline().strip())

words = [sys.stdin.readline().strip() for x in range(wordsNum)]

for i in range(wordsNum):
    stack = LifoQueue()

    for j in range(len(words[i])):
        if stack.empty():
            stack.put(words[i][j])
        else:
            topOfStack = stack.get()

            if topOfStack != words[i][j]:    
                stack.put(topOfStack)
                stack.put(words[i][j])
        
    if stack.empty():
        result += 1

sys.stdout.write(str(result) + '\n')
