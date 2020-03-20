import sys

from queue import LifoQueue

numOfTestCases = int(sys.stdin.readline())

result = []

for i in range(numOfTestCases):
    stack = LifoQueue()

    # PS : Parenthesis String
    PS = sys.stdin.readline().strip()

    isChecked = False

    # len(PS) - 1 이유는 sys.stdin.readline()으로 읽으면, 맨 끝에 \n까지 읽혀져서 그럼! 
    # 전에 split 쓸 땐, delimiter 특별히 지정 안 하면 공백(스페이스, 탭, 엔터 기준으로) 나눠줘서 고려 안 해도 되었던 것!
    # 또는 sys.stdin.readline().strip()하면, 맨 뒤 공백 문자 알아서 제거해줌! (지금은 이거로 바꿈)

    for j in range(len(PS)):
        if stack.empty():
            stack.put(PS[j])
        else:
            topOfStack = stack.get()
   
            if PS[j] == ")":
                if topOfStack != "(":
                    result += ["NO\n"]
                    isChecked = True
                    break
            else:
                stack.put(topOfStack)
                stack.put(PS[j])
    
    if not(isChecked) and stack.empty():
        result += ["YES\n"]
    elif not(isChecked) and not(stack.empty()):
        result += ["NO\n"]

[sys.stdout.write(x) for x in result]
