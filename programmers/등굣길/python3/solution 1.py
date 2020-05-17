import numpy as np

def solution(m, n, puddles):
    shortPath = np.zeros((m, n))

    for i in range(m):
        for j in range(n):
            if [i+1, j+1] in puddles:
                continue
            else:
                if i == 0 and j == 0:
                    shortPath[i, j] = 1
                elif i != 0 and j == 0:
                    shortPath[i, j] = shortPath[i-1, j]
                elif i == 0 and j != 0:
                    shortPath[i, j] = shortPath[i, j-1]
                else:
                    shortPath[i, j] = (shortPath[i-1, j] + shortPath[i, j-1]) % 1000000007
    
    return shortPath[m-1, n-1]
