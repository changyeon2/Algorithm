def solution(clothes):
    clothesDict = dict()

    if len(clothes) == 0:
        return 0
    elif len(clothes) == 1:
        return 1

    answer = 1

    for i in range(len(clothes)):
        if clothesDict.get(clothes[i][1]) == None:
            clothesDict[clothes[i][1]] = [clothes[i][0]]
        else:
            clothesDict[clothes[i][1]].append(clothes[i][0])

    for x in list(clothesDict.keys()):
        answer *= (len(clothesDict[x]) + 1)

    return (answer - 1)
