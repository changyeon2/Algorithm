# case 1 - 그냥 가는거
# case 2 - 점프 후 남은 거리 가기 (1. 점프 후 남은 거리, 2. 점프 한번 더해서 더 간 거리만큼 뒤로 가기)
# case 3 - 점프해서 한번에 가기

# 점프 후 남은 거리 가는 방법이 유효한, 즉 jumpNum >= 1인 경우는 점프 한번 더하고 뒤로 가는 경우보다 점프만 하는 경우가 항상 더 짧음!
# 그러나 유효하지 않은 jumpNum == 0의 경우는, 점프 한번 해서 뒤로 가는 경우보다 점프 두번 해서 가는 경우가 항상 짧다고 할 수 없다! 
# 그래서 이 경우는 유효하지 않은 경우 지우고, 점프 후 더 간 거리만큼 뒤로 가는 경우를 넣음!!

x, y, jumpDistance, jumpTime = map(int, input().split())

distance  = (x**2 + y**2)**0.5

jumpNum = distance // jumpDistance
remain = distance - jumpNum * jumpDistance

if jumpNum == 0:
    print(min(jumpTime + (jumpDistance - distance), distance, 2 * jumpTime))
else:
    print(min(jumpNum*jumpTime + remain, (jumpNum+1)*jumpTime, distance))

