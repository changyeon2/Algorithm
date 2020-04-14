def solution(genres, plays):
    musicDict = dict()
    playSum = dict()
    answer = []
    
    for i in range(len(genres)):
        if musicDict.get(genres[i]) == None:
            musicDict[genres[i]] = [(i, plays[i])]
            playSum[genres[i]] = plays[i]
        else:
            musicDict[genres[i]].append((i, plays[i]))
            playSum[genres[i]] += plays[i]
    
    genresList = list(musicDict.keys())
    genresList.sort(key=lambda x : playSum[x], reverse = True)
    
    for x in genresList:
        if len(musicDict[x]) == 1:
            answer.append(musicDict[x][0][0])
        else:
            musicDict[x].sort(key=lambda x : x[1], reverse=True)
            answer.append(musicDict[x][0][0])
            answer.append(musicDict[x][1][0])
            
    
    return answer
