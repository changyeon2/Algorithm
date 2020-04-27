class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        longestLen = 0
        
        for i in range(0, len(s)):
            len1 = self.IsPossibleToExpand(s, i, i)
            len2 = self.IsPossibleToExpand(s, i, i+1)
            
            longestLen = max(len1, len2)
            
            if longestLen > end - start + 1:
                start = i - (longestLen - 1) // 2
                end = i + longestLen // 2
        
        return s[start : end+1]
            
    def IsPossibleToExpand(self, s: str, head: int, tail: int) -> int:
        
        while head >= 0 and tail < len(s) and s[head] == s[tail]:
            head -= 1
            tail += 1
            
        # 원래 길이에서 -2 (while문을 유효하지 않는 경우를 거치고 나서 탈출하므로 +2가 더 된 상태 -> -2를 하고 return! )
        return tail - head - 1
        
