# solution 1 - 직접 교점 구해서 수선 내릴 수 있는지 따져보는 방식 -> 더 메모리 많이쓰고, 오래 걸림)
def getLine(start, end):
    startPt = start
    endPt = end
    if start[0] - end[0] == 0:
        grad = float("inf")
        constant = 0
    else :
        if start[1] - end[1] == 0:
            grad = 0
            constant = start[0]
        else:
            grad = (start[1] - end[1]) / (start[0] - end[0])
            constant = start[1] - grad * start[0]

    return [grad, startPt, endPt, constant]

def isOntheLine(line, point):
    if line[0] == float("inf"):
        if line[1][1] > line[2][1]:
            if point[1] <= line[1][1] and point[1] >= line[2][1]:
                return True
            else:
                return False
        else:
            if point[1] >= line[1][1] and point[1] <= line[2][1]:
               return True
            else:
                return False
    elif line[0] == 0:
        if line[1][0] > line[2][0]:
            if point[0] <= line[1][0] and point[0] >= line[2][0]:
                return True
            else:
                return False
        else:
            if point[0] >= line[1][0] and point[0] <= line[2][0]:
               return True
            else:
                return False
    else:
        verticalGrad = (-1) * 1 / line[0]
        constant = point[1] - verticalGrad * point[0]

        intersactXcor = (constant - line[3]) / (line[0] - verticalGrad)

        if line[1][0] > line[2][0]:
            if (intersactXcor <= line[1][0] and intersactXcor >= line[2][0]):
                return True
            else:
                return False
        else:
            if (intersactXcor >= line[1][0] and intersactXcor <= line[2][0]):
                return True
            else:
                return False

def getDistanceBetweenPointAndLine(line, point):
    if line[0] == float("inf"):
        return abs(line[1][0] - point[0])
    elif line[0] == 0:
        return abs(line[1][1] - point[1])
    else:
        return (abs(line[0]*point[0] - point[1] + line[3]) / (line[0]**2 + 1)**(0.5))

def getDistanceBetweenPoints(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**(0.5)

numOfSinchon, numOfAnam = map(int, input().split())

sinchonRoad = dict()
anamRoad = dict()

closeDistance = []

# i += 1과 같이 for문의 iterator를 바꾸는 것은 이 for문 돌아가는 것에 아무 영향을 안 줌!!
for i in range(0, numOfSinchon):
    temp1 = [float(x) for x in input().split()]
    sinchonRoad[i] = getLine((temp1[0], temp1[1]), (temp1[2], temp1[3]))   

for i in range(0, numOfAnam):
    temp2 = [float(x) for x in input().split()]
    anamRoad[i] = getLine((temp2[0], temp2[1]), (temp2[2], temp2[3]))   

closeDistance = -1

for i in range(0, numOfSinchon):
    for j in range(0, numOfAnam):
        distance = min(getDistanceBetweenPoints(sinchonRoad[i][1], anamRoad[j][1])\
            , getDistanceBetweenPoints(sinchonRoad[i][1], anamRoad[j][2]) \
            , getDistanceBetweenPoints(sinchonRoad[i][2], anamRoad[j][1]) \
            , getDistanceBetweenPoints(sinchonRoad[i][2], anamRoad[j][2]))

        if isOntheLine(anamRoad[j], sinchonRoad[i][1]):
            distance = min(distance, getDistanceBetweenPointAndLine(anamRoad[j], sinchonRoad[i][1]))
        if isOntheLine(anamRoad[j], sinchonRoad[i][2]):
            distance = min(distance, getDistanceBetweenPointAndLine(anamRoad[j], sinchonRoad[i][2]))

        if isOntheLine(sinchonRoad[i], anamRoad[j][1]):
            distance = min(distance, getDistanceBetweenPointAndLine(sinchonRoad[i], anamRoad[j][1]))
        if isOntheLine(sinchonRoad[i], anamRoad[j][2]):
            distance = min(distance, getDistanceBetweenPointAndLine(sinchonRoad[i], anamRoad[j][2]))

        if closeDistance == -1:
            closeDistance = distance
        else:
            closeDistance = min(closeDistance, distance)

print(closeDistance)
