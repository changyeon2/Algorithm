import itertools

def solution(numbers):
    answer = 0
    # itertools.permutations return 값은 쌓여있지 않은?? 튜플들이라 
    # 각 원소에 튜플->문자열로 바꿔주는 함수 적용 뒤 list화! (list()를 해야지 []로 씌우면 안 됨!)

    allCases = set()
    
    for i in range(0, len(numbers)):
        # list 화 -> 각 원소에 int() 적용 -> set에 추가
        [allCases.add(y) for y in [int(x) for x in list(map(''.join, itertools.permutations(numbers, i+1)))]]
    
    # set을 indexing을 위해 list로 
    allCases = list(allCases)
    
    for i in range(len(allCases)):
        if isPrime(allCases[i]):
            answer += 1

    return answer

def isPrime(number):
    if number == 0 or number == 1:
        return False
    else:
        for i in range(2, int(number**(0.5) + 1)):
            if int(number) % i == 0:
                return False
        
        return True

print(solution('011'))
