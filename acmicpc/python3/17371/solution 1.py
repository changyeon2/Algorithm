# main idea : (최소 거리 + 최대 거리)를 최소화하는 거니까 최소거리 자체를 0으로(최소로) 한뒤에, 최대거리만을 최소화해보자!

def findthefarthest(index, Dict, N):
    farIndex = 0
    farDistance = 0

    for i in range(0, N):
        distance = (Dict[i][0] - Dict[index][0])**2 + (Dict[i][1] - Dict[index][1])**2

        if farDistance < distance:
            farIndex = i
            farDistance = distance

    return [farIndex, farDistance]


numOfStore = int(input())

cor = dict()

farCor = dict() # i : [farIndex, farDistance]

for i in range(0, numOfStore):
    cor[i] = [int(x) for x in input().split()]

for i in range(0, numOfStore):
    farCor[i] = findthefarthest(i, cor, numOfStore)

answer = 0
sumOfDistance = farCor[0][1]

for i in range(0, numOfStore):
    if sumOfDistance > farCor[i][1]:
        answer = i
        sumOfDistance = farCor[i][1]

print(str(cor[answer][0]) + " " + str(cor[answer][1]))
