class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        
        indexDict = dict()
        
        i = 0
        j = 0
        
        # using sliding window
        
        for j in range(0, len(s)):
            if indexDict.get(s[j]) != None:
                i = max(indexDict[s[j]], i)
            
            indexDict[s[j]] = j+1
            maxlen = max(j-i+1, maxlen)
        
        return maxlen
