# main idea : quickSort로 str(A) + str(B)과 str(B) + str(A)를 비교하여(string compare) 정렬하는데, 
#             한 가지 예외 상황만 따로 처리해주면 됨! -> 모든 원소가 0인 경우는 0000..이 아닌 0으로만 출력!

def solution(numbers):
    zeroArray = [0] * len(numbers)
    isAllZero = True
    
    for i in range(len(numbers)):
        if zeroArray[i] != numbers[i]:
            isAllZero = False
    
    if isAllZero:
        return "0"
    else:
        numbers = quickSort(numbers)

        return "".join(str(x) for x in numbers)

def quickSort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    center = numbers[(len(numbers)-1) // 2]
    
    small = []
    equal = []
    big = []
    
    for num in numbers:
        if str(num) + str(center) < str(center) + str(num):
            small.append(num)
        elif str(num) + str(center) == str(center) + str(num):
            equal.append(num)
        else:
            big.append(num)
    
    return quickSort(big) + equal + quickSort(small)
