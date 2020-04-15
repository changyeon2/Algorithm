def solution(brown, red):
    divisors = findDivisor(brown+red)
    
    for height in divisors: 
        width = (brown+red) // height
        
        if 2*width + 2*(height-2) == brown:
            return [width, height]
    

def findDivisor(number):
    divisors = []
    for i in range(1, int(number**(0.5))+1):
        if number % i == 0:
            divisors.append(i)
    
    return divisors
