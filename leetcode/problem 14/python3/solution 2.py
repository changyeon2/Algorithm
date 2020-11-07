# Using binary search

class Solution:    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        else:
            target = strs[0]
            
            # strs가 element 한 개만 가지면, 
            # list slicing 했을 때 remains가 [] (empty list)가 되므로, 따로 handling!
            remains = strs[1:]
            
            if not remains:
                return target
            
            left = 0
            right = len(strs[0]) - 1
            
            # list[0:0]하면 []가 됨!!
            
            mid = ((left + right) // 2)
            
            while left <= right:
                # mid + 1 하는 이유는, 즉, mid를 포함시키는 이유는,
                # mid가 0인 경우에 [0:mid]를 해버리면 [0:0]이 되어서 [](empty list)가 때문!!
                # 그냥 length로 subset한다고 생각!
                
                # mid는 왼쪽 부분이 commonPrefix인 경우, 그 값이 커지기 때문에 
                # 기존에 append하기 보단, 다시 subset하면 됨!! 
                # 따라서 (기존 lcp) + target[left:mid] 할 필요가 없음!
                if self.isCommonPrefix(target[0:mid+1], remains):
                    left = mid + 1
                else:
                    right = mid - 1
                
                mid = ((left + right) // 2)
            
            return target[0:mid+1]
    
    def isCommonPrefix(self, target, remains):
        for x in remains:
            if not(x.startswith(target)):
                return False
        return True
