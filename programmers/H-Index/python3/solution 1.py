def solution(citations):
    # 큰 순서대로 정렬(큰 수 카운팅 쉽게 하려고)
    citations.sort(reverse=True)
    
    for i in range(len(citations), -1, -1):
        # hIndex의 범위 (0 ~ len(citations))
        hIndex = i
        
        count = 0
        
        for j in range(0, len(citations)):
            if citations[j] < hIndex and count >= hIndex:
                return hIndex
            elif citations[j] < hIndex and count < hIndex:
                break
            else:
                count += 1
        
        # 저 첫번째 조건에 안 걸리고, 쭈루룩 다 통과하는 경우도 유효한 경우! -> 체크해줌
        if count == len(citations):
            return hIndex
