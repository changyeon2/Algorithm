# main idea : 1. 알파벳이면 바로 postfix에 추가 
#             2. '('면 stack에 곧바로 추가, 그리고 ')'가 나오면 '('가 나올 때까지 pop하며 postfix에 추가,
#             3. '*', '/' 가 나오면 (not(stack.empty()) and (topOfStack == '*' or topOfStack == '/')) 때가지만 pop하며 postfix에 추가,
#                '+', '-'가 나오면 (not(stack.empty()) and topOfStack != '(')때까지만 pop하며 postfix에 추가!

import sys
from collections import deque

stack = deque()

infix = sys.stdin.readline().rstrip()

postfix = ""

for i in range(len(infix)):
    if ord(infix[i]) >= 65 and ord(infix[i]) <= 90:
        postfix += infix[i]

    elif infix[i] == "(":
        stack.append("(")

    elif infix[i] == ")":
        while stack[-1] != "(":
            postfix += stack.pop()

        # delete "("
        stack.pop()

    elif infix[i] == "*" or infix[i] == "/":
        while stack and (stack[-1] == "*" or stack[-1] == "/"):
            postfix += stack.pop()

        stack.append(infix[i])

    elif infix[i] == "+" or infix[i] == "-":
        while stack and stack[-1] != "(":
            postfix += stack.pop()

        stack.append(infix[i])

while stack:
    postfix += stack.pop()

sys.stdout.write(postfix + "\n")
