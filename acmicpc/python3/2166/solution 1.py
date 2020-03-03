def crossProduct(first_x, first_y, second_x, second_y, third_x, third_y):
    return (second_x - first_x)*(third_y - first_y) - (second_y - first_y)*(third_x - first_x)

numOfPoints = int(input())

point = dict()

subArea = 0
area = 0

for i in range(0, numOfPoints):
    xcor, ycor = [int(t) for t in input().split()]
    point[i] = [xcor, ycor]

basePoint = [point[0][0], point[0][1]]

for i in range(1, numOfPoints - 1):
    subArea = crossProduct(point[i][0], point[i][1], basePoint[0], basePoint[1], point[i+1][0], point[i+1][1])
    area += subArea

if area < 0:
    area *= (-1)

area = round(0.5 * area, 2)

print(area)
