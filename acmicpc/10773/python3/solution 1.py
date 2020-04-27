import sys

from queue import LifoQueue

stack = LifoQueue()

numOfInt = int(sys.stdin.readline())

result = 0

for i in range(numOfInt):
    integer = int(sys.stdin.readline())

    if integer == 0:
        stack.get()
    else:
        stack.put(integer)

while not(stack.empty()):
    result += stack.get()

sys.stdout.write(str(result) + '\n')

