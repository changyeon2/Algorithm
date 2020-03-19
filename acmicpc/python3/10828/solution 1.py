# LifoQueue는 Stack과 동일한 개념!
# maxsize 설정하면 더 좋을 듯?? 메모리 측면에서

import sys

from queue import LifoQueue

stack = LifoQueue()

numOfCMD = int(sys.stdin.readline())

result = []

for i in range(numOfCMD):
    CMD = sys.stdin.readline().split()

    if CMD[0] == "push":
        CMD[1] = int(CMD[1])
        stack.put(CMD[1])

    elif CMD[0] == "pop":
        if stack.empty():
            result += ['-1\n']
        else:
            result += [str(stack.get())+'\n']

    elif CMD[0] == "size":
        result += [str(stack.qsize())+'\n']

    elif CMD[0] == "empty":
        if stack.empty():
           result += ['1\n']
        else:
            result += ['0\n']

    elif CMD[0] == "top":
        if stack.empty():
            result += ['-1\n']
        else:
            top = stack.get()
            stack.put(top)
            result += [str(top)+'\n']

[sys.stdout.write(x) for x in result]
