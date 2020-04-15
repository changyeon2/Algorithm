def solution(citations):
    citations.sort()
    
    length = len(citations)
    
    # h-index의 정의 이용!! 큰 것들의 개수가 h-index의 후보가 됨(0 ~ length개까지)
    # 여기서는 1 ~ length개인경우 체크(0인 경우는 IndexError 뜸(out of range))
    for i in range(length):
        if citations[i] >= length - i:
            return length - i
    
    # 여기서 h-index 0인 경우 
    return 0
    
