first_x, first_y = [int(x) for x in input().split()]
second_x, second_y = [int(x) for x in input().split()]
third_x, third_y = [int(x) for x in input().split()]

crossProduct = (second_x - first_x)*(third_y - first_y) - (second_y - first_y)*(third_x - first_x)

if crossProduct > 0:
    print(1)
elif crossProduct == 0:
    print(0)
else:
    print(-1)
