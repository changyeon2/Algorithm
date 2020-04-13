def solution(phone_book):
    # string 정렬하면, 앞글자에 따라 알아서 정렬됨! ex) 12, 123, 56, 567 이렇게!
    phone_book.sort()
    
    # zip(list1, list2)은 각각의 리스트에서 같은 인덱스의 원소끼리 매칭해줌! (ex) (list1[0], list2[0]), ...)
    for str1, str2 in zip(phone_book[:-1], phone_book[1:]):
        if str2.startswith(str1):
            return False
    
    return True
