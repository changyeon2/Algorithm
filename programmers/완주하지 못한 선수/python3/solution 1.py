def solution(participant, completion):
    partDict = dict()
    
    for i in range(len(participant)):
        if partDict.get(participant[i]) == None:
            partDict[participant[i]] = 1
        else:
            partDict[participant[i]] += 1
            
    for i in range(len(completion)):
        partDict[completion[i]] -= 1
        
        if partDict[completion[i]] == 0:
            del partDict[completion[i]]
    
    answer = list(partDict.keys())[0]
    return answer
