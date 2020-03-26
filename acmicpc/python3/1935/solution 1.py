# main idea : 후위표기법 1번 문제와는 다르게, 이번엔 operand를 stack에 넣음! (중간중간 operator를 이용해 연산한 결과값도 스택에 넣음!)

import sys
from collections import deque

stack = deque()

numOfOperand = int(sys.stdin.readline().rstrip())

postfix = sys.stdin.readline().rstrip()

operandDict = dict()

for i in range(numOfOperand):
    operandDict[chr(65+i)] = int(sys.stdin.readline().rstrip())

for i in range(len(postfix)):
    if ord(postfix[i]) >= 65 and ord(postfix[i]) <= 90:
        stack.append(operandDict[postfix[i]])
    else:
        secondOperand = stack.pop()
        firstOperand = stack.pop()

        if postfix[i] == "+":
            stack.append(firstOperand + secondOperand)
        elif postfix[i] == "-":
            stack.append(firstOperand - secondOperand)
        elif postfix[i] == "*":
            stack.append(firstOperand * secondOperand)
        elif postfix[i] == "/":
            stack.append(firstOperand / secondOperand)

sys.stdout.write("{:.2f}".format(stack.pop()) + '\n')
