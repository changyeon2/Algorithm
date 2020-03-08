# solution 2 : dot product로 수선 내릴 수 있는지 확인하는 방법
import sys

def isPossibleToMakeALine(line, point):
    vec1 = (point[0] - line[0][0], point[1] - line[0][1])
    vec2 = (line[1][0] - line[0][0], line[1][1] - line[0][1])

    dotProduct1 = (vec1[0] * vec2[0] + vec1[1] * vec2[1])

    vec3 = (point[0] - line[1][0], point[1] - line[1][1])
    vec4 = (line[0][0] - line[1][0], line[0][1] - line[1][1])

    dotProduct2 = (vec3[0] * vec4[0] + vec3[1] * vec4[1]) 

    if dotProduct1 < 0 or dotProduct2 < 0:
        return False
    else:
        return True

def getDistanceBetweenPointAndLine(line, point):
    # a*sin(theta) 구하기 (이때 a는 선분의 거리)
    return abs(crossProduct(line[1][0] - line[0][0], line[1][1] - line[0][1], point[0] - line[0][0], point[1] - line[0][1])) / getDistanceBetweenPoints1(line[0], line[1])

def getDistanceBetweenPoints1(point1, point2): 
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**(0.5)

def getDistanceBetweenPoints2(point1, point2): 
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def crossProduct(first_x, first_y, second_x, second_y):
    return second_y * first_x - second_x * first_y 

numOfSinchon, numOfAnam = map(int, sys.stdin.readline().split())

sinchonRoad = dict()
anamRoad = dict()

for i in range(0, numOfSinchon):
    temp = [float(x) for x in sys.stdin.readline().split()]
    sinchonRoad[i] = ((temp[0], temp[1]), (temp[2], temp[3]))   

for i in range(0, numOfAnam):
    temp = [float(x) for x in sys.stdin.readline().split()]
    anamRoad[i] = ((temp[0], temp[1]), (temp[2], temp[3]))   

closeDistance = -1

for i in range(0, numOfSinchon):
    for j in range(0, numOfAnam):
        distance = min(getDistanceBetweenPoints2(sinchonRoad[i][0], anamRoad[j][0])\
            , getDistanceBetweenPoints2(sinchonRoad[i][0], anamRoad[j][1]) \
            , getDistanceBetweenPoints2(sinchonRoad[i][1], anamRoad[j][0]) \
            , getDistanceBetweenPoints2(sinchonRoad[i][1], anamRoad[j][1]))**(0.5)

        if isPossibleToMakeALine(anamRoad[j], sinchonRoad[i][0]):
            distance = min(distance, getDistanceBetweenPointAndLine(anamRoad[j], sinchonRoad[i][0]))
        if isPossibleToMakeALine(anamRoad[j], sinchonRoad[i][1]):
            distance = min(distance, getDistanceBetweenPointAndLine(anamRoad[j], sinchonRoad[i][1]))
        if isPossibleToMakeALine(sinchonRoad[i], anamRoad[j][0]):
            distance = min(distance, getDistanceBetweenPointAndLine(sinchonRoad[i], anamRoad[j][0]))
        if isPossibleToMakeALine(sinchonRoad[i], anamRoad[j][1]):
            distance = min(distance, getDistanceBetweenPointAndLine(sinchonRoad[i], anamRoad[j][1]))
       
        if closeDistance < 0:
            closeDistance = distance
        else:
            if closeDistance > distance:
                closeDistance = distance

print(closeDistance)

