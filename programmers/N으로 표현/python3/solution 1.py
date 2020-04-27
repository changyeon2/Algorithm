def solution(N, number):
    memo = dict()

    [memo.update({i : set()}) for i in range(1, 9)]

    for i in range(1, 9):
        memo[i].add(N * (10**(i)-1) // 9)

        for j in range(1, i):
            for k in memo[j]:
                for l in memo[i-j]:
                    memo[i].add(k+l)
                    memo[i].add(k-l)
                    memo[i].add(k*l)

                    if l != 0:
                        memo[i].add(k//l)

        if number in memo[i]:
            return i

    return -1
