def solution(N):
    sides = [1, 1]
    perimeters = [4]
    
    for i in range(1, N):
        if i >= 2:
            sides.append(sides[i-2]+sides[i-1])
        
        perimeters.append(perimeters[i-1] + 2*sides[i])
        
    return perimeters[N-1]
