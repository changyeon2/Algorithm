# 알게된 중요한 사실 : queue.lifoqueue는 fully thread-safe라는 기능을 위해 고안되었고,
#                 그렇기에, 저 기능을 유지하기 위해 매 operation마다 약간의 시간을 더 씀!! -> 느릴 수 있다.
#                 이 fully thread-safe가 필요하지 않는 이상, lifoqueue보단 collection.deque를 쓰자!

import sys

from collections import deque

noteNum, fretNum = [int(x) for x in sys.stdin.readline().split()]

moveNum = 0

stringDict = dict()

[stringDict.update({i: deque(maxlen=fretNum)}) for i in range(1, 7)]

for i in range(noteNum):
    stringToPush, fretToPush = [int(x) for x in sys.stdin.readline().split()]
    
    while True:
        if len(stringDict[stringToPush]) == 0:
            moveNum += 1
            stringDict[stringToPush].append(fretToPush)
            break
        else:
            topOfStack = stringDict[stringToPush].pop()

            if topOfStack < fretToPush:
                moveNum += 1
                stringDict[stringToPush].append(topOfStack)
                stringDict[stringToPush].append(fretToPush)
                break
            elif topOfStack == fretToPush:
                stringDict[stringToPush].append(topOfStack)
                break
            else:
                moveNum += 1
        
sys.stdout.write(str(moveNum) + '\n')
