class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rowDict = dict()
        
        result = ""
        
        add = True
        
        k = 0
        
        for i in range(0, numRows):
            block[i] = []
        
        for j in range(0, len(s)):
            block[k] += s[j]
            
            if add == True:
                k += 1
            else:
                k -= 1
            
            if k == numRows:
                if numRows >= 3:
                    k -= 2
                    add = False
                else:
                    k = 0
            
            if k == 0:
                add = True
        
        for t in range(0, len(block)):
            for p in range(0, len(block[t])):
                result += block[t][p]
        
        return result
    
    # 좀 더 최적화해보기!!
           
