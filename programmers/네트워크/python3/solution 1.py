def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        if not(visited[i]):
            dfs(n, computers, visited, i)       
            answer += 1
    
    return answer

def dfs(n, computers, visited, curIdx):
    visited[curIdx] = True

    for i in range(n):
        if i == curIdx:
            continue
        if not(visited[i]) and computers[curIdx][i] == 1:
            dfs(n, computers, visited, i)

    return
