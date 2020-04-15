import itertools

def solution(baseball):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    allCases = list(map(''.join, itertools.permutations(numbers, 3)))
    
    answer = 0

    for x in allCases:
        if x[0] == x[1] or x[1] == x[2] or x[2] == x[0]:
            allCases.remove(x)
            continue
        
        answerCount = 0

        for y in baseball:
            [testNum, strike, ball] = y
            testNum = str(testNum)

            for i in range(3):
                for j in range(3):
                    if x[i] == testNum[j] and i == j:
                        strike -= 1
                    elif x[i] == testNum[j] and i != j:
                        ball -= 1
            
            if strike == 0 and ball == 0:
                answerCount += 1
            else:
                break
        
        if answerCount == len(baseball):
            answer += 1
                
    return answer
