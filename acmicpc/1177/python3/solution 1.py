# main idea : 조쌤에 대한 상대벡터로 만들어서 학생들에 대한 벡터만 가지고 문제를 풀자!
# -> 결국 경우의 수는 radius가 형성하는 원이 만드는 영역에 1. 항상 들어와있는 애, 2. 들어왔다 나가는 애 뿐!
# 학생들이 linear하게 움직이므로 나갔다가 들어오는 경우는 없다!
# 결국 상대 벡터의 크기가 radius와 같은 경우를 조사하면 1의 경우에는 이차식 자체가 형성이 안 될 것이고(혹은, determinant가 <0) (대신 이 경우에 상수항 체크는 필수!)
# 따라서, 1의 경우는 항상 count해둠!
# 2의 경우인 들어왔다 나가는 애는 반드시 두개의 근을 가진다!(determinant >= 0 & 중근도 두개의 근으로 취급)
# 그러면 언제까지 특정 학생을 셀 수 있는지 어떻게 아냐?
# -> 근의 두개니까 방문 순서대로(시간 순서대로) 정리한 뒤에 또 다른 근이 나오기 전까지, 즉 거리가 radius가 다시 되어 원의 영역 밖으로 나가기 전까진 그 점이 유효하다는 점을 이용!
# 나갈 때 count에서 1을 뺀다!

import sys

runnerNum, tracerRadius, tracerXCor, tracerYCor, tracerXVelo, tracerYVelo = [int(x) for x in sys.stdin.readline().split()]

tracerCor = [tracerXCor, tracerYCor]
tracerVelo = [tracerXVelo, tracerYVelo]

validRunner = []
visited = dict()

count = 0
validNum = 0

for i in range(0, runnerNum):
    runnerRelVec = [int(x) for x in sys.stdin.readline().split()] # i : [xCor, yCor, xVelo, yVelo]
    X = (runnerRelVec[0] - tracerCor[0])
    Y = (runnerRelVec[1] - tracerCor[1])
    VX = (runnerRelVec[2] - tracerVelo[0]) 
    VY = (runnerRelVec[3] - tracerVelo[1])

    a = (VX*VX + VY*VY)
    b = 2 * (VX*X + VY*Y)
    c = (X*X + Y*Y - tracerRadius*tracerRadius)

    determinant = b*b - 4*a*c

    if determinant < 0 or a==0:
        if c <= 0:
            count += 1
    else:
        t1 = max(((-b - determinant**0.5) / (2*a)), 0)
        t2 = (-b + determinant**0.5) / (2*a)

        if t2 >= 0:
            visited[i] = False
            validRunner += [(t1, i)]
            validRunner += [(t2, i)]

validRunner = sorted(validRunner, key=lambda x: x[0])

maxCatchNum = count

for i in range(0, len(validRunner)):
    if visited[validRunner[i][1]] :
        count -= 1
    else:
        visited[validRunner[i][1]] = True
        count += 1
        maxCatchNum = max(maxCatchNum, count)

print(maxCatchNum)
