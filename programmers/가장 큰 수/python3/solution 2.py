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
        # 첫번째 형태가 더 크면 음수 반환
        return -1
    elif str1 + str2 == str2 + str1:
        # 같으면 제자리
        return 0
    else:
        # 첫번째 형태가 두번째 변형 꼴??(순서를 변경한 꼴)보다 작으면 양수 반환!
        return 1
    
    # 그냥 간단하게 str1이 str2보다 큰 상태로 유지시키고 싶으면 -1, 작은 상태로 바꾸고 싶으면 1인 듯
    
