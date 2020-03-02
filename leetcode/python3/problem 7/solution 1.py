class Solution:
    def reverse(self, x: int) -> int:
        isNeg = False
        
        if x < 0:
            isNeg = True
            x = -x
            
        digitDict = dict()
        result = 0
        
        index = 0
        length = 1
        
        if x < 10:
            result = x
        else:
            while x >= 10:
                digitDict[index] = (x % 10)
                index += 1
                x = x // 10
                length += 1
                
            digitDict[index] = x
        
            for i in range(0, length):
                result += digitDict[i] * (10 ** (length - i - 1))
        
        
        if result < -(2**31) or result > 2**31 - 1:
            return 0
        else:
            if isNeg == True:
                result *= (-1)
            return result
        
