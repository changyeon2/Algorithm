# main idea : ccw로 선분 간 위치 파악 후, union-find 이용!

import sys

def ccw(x1, y1, x2, y2, x3, y3):
    crossProduct = (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)

    if crossProduct > 0:
        return 1
    elif crossProduct == 0:
        return 0
    else:
        return -1

def comp(point1, point2):
    if point1[0] == point2[0]:
        return point1[1] >= point2[1]
    else:
        return point1[0] >= point2[0]

def checkValid(line1, line2):
    p1 = line1[:2]
    p2 = line1[2:4]
    q1 = line2[:2]
    q2 = line2[2:4]

    if comp(p1, p2):
        p1, p2 = p2, p1
    if comp(q1, q2):
        q1, q2 = q2, q1

    return comp(q2, p1) and comp(p2, q1)
    
def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return
    else:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
            nodeCount[root_x] += nodeCount[root_y]
        else:
            parent[root_x] = root_y
            nodeCount[root_y] += nodeCount[root_x]

            if rank[root_x] == rank[root_y]:
                rank[root_y] += 1

def checkIntersect(line1, line2):
    value1 = ccw(line1[0], line1[1], line1[2], line1[3], line2[0], line2[1]) * ccw(line1[0], line1[1], line1[2], line1[3], line2[2], line2[3])
    value2 = ccw(line2[0], line2[1], line2[2], line2[3], line1[0], line1[1]) * ccw(line2[0], line2[1], line2[2], line2[3], line1[2], line1[3])

    if value1 == 0 and value2 == 0:
        if checkValid(line1, line2):
            return True
        else:
            return False

    return (value1 <= 0 and value2 <= 0)
        
lineSegNum = int(sys.stdin.readline())

parent = [i for i in range(lineSegNum)]
rank = [0 for i in range(lineSegNum)]
nodeCount = [1 for i in range(lineSegNum)]

line = [[float(x) for x in sys.stdin.readline().split()] for y in range(lineSegNum)] # [x1, y1, x2, y2]

for i in range(0, lineSegNum-1):
    for j in range(i+1, lineSegNum):
        if checkIntersect(line[i], line[j]):
            union(i, j)

groupNum = 0

for i in range(0, lineSegNum):
    if parent[i] == i:
        groupNum += 1

print(groupNum)
print(max(nodeCount))
