def solution(budgets, M):
    budgets.sort()
    answer = binarySearch(budgets, M)
    return answer

def binarySearch(budgets, M):
    answer = 0

    left = 1
    right = budgets[-1]
    
    while(left<=right):
        mid = (left+right) // 2
        sumOfBudgets = 0
    
        for i in range(len(budgets)):
            if budgets[i] >= mid:
                sumOfBudgets += mid*(len(budgets)-i)
                break
            else:
                sumOfBudgets += budgets[i]

        if sumOfBudgets <= M:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
            
    # mid로 하게 되면, sumOfBudgets > M의 유효하지 않는 경우를 거치고 끝날 수도 있어서, 오답 발생!
    return answer
        
