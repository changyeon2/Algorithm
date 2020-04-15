# main idea : 내부적으로 quickSort로 구현되어있다는 점을 이용.
#             따라서 quickSort 다 구현 필요없이, functools.cmp_to_key로
#             small, big, equal를 나누는 '기준'만 정해주면 됨!

from functools import cmp_to_key

def solution(numbers):
    strings = [str(x) for x in numbers]
    strings.sort(key=cmp_to_key(compare))
    
    return str(int("".join(strings)))

def compare(str1, str2):
    if str1 + str2 > str2 + str1:
        # 오른쪽으로 보냄!
        return -1
    elif str1 + str2 == str2 + str1:
        # 제자리
        return 0
    else:
        # 왼쪽으로 보냄!
        return 1
    
