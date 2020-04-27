# main idea : 선분과 사각형의 각 변을 이용, ccw로 관계 파악. 그리고 세부적인 케이스 핸들링
# 먼저 ccw 값을 기준으로 경우 나눔. 
# (value1 <= 0, value2 <= 0)이 유효한 경우인데, 모두 0인 경우는 나올 수 있는 경우의 수가 여러개 있으므로 특별히 이를 validation하는 함수를 만듦.
# 모두 0인 경우는 크게 3개로 나눌 수 있음. 
# (1. 명백하게 겹쳐서(끝점의 겹침없이) value1, value2가 모두 0인 경우)
# (2. 각 끝점이 같아서 value1, value2가 모두 0인 경우)
# 이때 2의 경우에는 
# 1. 끝점이 같고 겹치는 경우(p1=q1 or p2=q2이고 isOnTheLine이 True인 경우)와
# 2. 끝점은 같지만 겹치지 않는 경우가 있음(p1=q1 or p2=q2이지만 isOnTheLine이 False인 경우 & p1=q2 or p2=q1인 경우)

import sys

def ccw(x1, y1, x2, y2, x3, y3):
    crossProduct = (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)

    if crossProduct > 0:
        return 1
    elif crossProduct == 0:
        return 0
    else:
        return -1

def comp1(point1, point2):
    if point1[0] == point2[0]:
        return point1[1] > point2[1]
    else:
        return point1[0] > point2[0]

def comp2(point1, point2):
    return (point1[0] == point2[0] and point1[1] == point2[1])

def checkIsOnTheLine(point, linePt1, linePt2):
    vec1 = [point[0] - linePt1[0], point[1] - linePt1[1]]
    vec2 = [linePt2[0] - linePt1[0], linePt2[1] - linePt1[1]]

    if (vec1[0] == 0 and vec1[1] == 0):
        return True

    cosTheta = abs(vec1[0] * vec2[0] + vec1[1] * vec2[1]) \
        / ((vec1[0]*vec1[0] + vec1[1]*vec1[1])**(0.5) * (vec2[0]*vec2[0] + vec2[1]*vec2[1])**(0.5))

    if cosTheta == 1:
        return True

    return False

def checkValid(line1, line2):
    p1 = line1[:2]
    p2 = line1[2:4]
    q1 = line2[:2]
    q2 = line2[2:4]

    # p2, q2에 큰 점(comp1 기준 참고) 배정 (이렇게하면 분석이 용이함)
    if comp1(p1, p2):
        p1, p2 = p2, p1
    if comp1(q1, q2):
        q1, q2 = q2, q1

    # 무조건 사이에서 만나는 경우(끝점끼리 만나지 않고, 명백하게 겹치는 경우)
    if comp1(q2, p1) and comp1(p2, q1) and not(comp2(p1, q1)) and not(comp2(p2, q2)):
        return 1
    
    # p1과 q1, p2와 q2가 같은 경우
    if comp2(p1, q1):
        if not(checkIsOnTheLine(p2, q1, q2)):
            return 0
        else:
            return 1

    if comp2(p2, q2): 
        if not(checkIsOnTheLine(p1, q1, q2)):
            return 0
        else:
            return 1

    # p1과 q2, p2와 q1이 같은 경우
    if comp2(q2, p1) or comp2(p2, q1):
        return 0
    
    return -1

def checkIntersect(square, line):
    intersectNum = 0
    isCorner = 0

    leftTop = square[0]
    leftBottom = square[2]
    rightTop = square[1]
    rightBottom = square[3]

    squareSide = [leftTop + rightTop, rightTop + rightBottom, rightBottom + leftBottom, leftBottom + leftTop]

    for i in range(4):
        value1 = ccw(squareSide[i][0], squareSide[i][1], squareSide[i][2], squareSide[i][3], line[0], line[1]) * ccw(squareSide[i][0], squareSide[i][1], squareSide[i][2], squareSide[i][3], line[2], line[3])
        value2 = ccw(line[0], line[1], line[2], line[3], squareSide[i][0], squareSide[i][1]) * ccw(line[0], line[1], line[2], line[3], squareSide[i][2], squareSide[i][3])
    
        if value1 == 0 and value2 == 0:
            flag = checkValid(squareSide[i], line)
            
            if flag == -1:
                continue
            elif flag == 0:
                intersectNum += 1
                isCorner += 1
            elif flag == 1:
                # 선분과 사각형의 한 변이 서로 겹침
                return 4

        elif (value1 <= 0 and value2 <= 0):
            if value2 == 0:
                isCorner += 1
            intersectNum += 1
    
    # 중복 카운팅 된 것은 빼주기!!
    deleteDup = isCorner//2

    for i in range(deleteDup):
        intersectNum -= 1

    if intersectNum == 2:
        return 2
    elif intersectNum == 1:
        return 1
    elif intersectNum == 0:
        return 0

### main ###

numOfTestCase = int(sys.stdin.readline())
result = []

for i in range(numOfTestCase):
    squarePoints = [int(x) for x in sys.stdin.readline().split()]

    square = [[squarePoints[0], squarePoints[3]], [squarePoints[2], squarePoints[3]],\
        [squarePoints[0], squarePoints[1]], [squarePoints[2], squarePoints[1]]]

    lineSeg = [int(x) for x in sys.stdin.readline().split()]

    result += [checkIntersect(square, lineSeg)]

[print(result[i]) for i in range(len(result))]
