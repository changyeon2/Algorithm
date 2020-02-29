class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keyIsValueDict = dict()
        
        for i in range(0, len(nums)):
            keyIsValueDict[nums[i]] = i
            
        for i in range(0, len(nums)):
            complement = target - nums[i]
            
            if keyIsValueDict.get(complement) != None and keyIsValueDict[complement] != i :
                if nums[i] > complement:
                    return [keyIsValueDict[complement], i]
                else:
                    return [i, keyIsValueDict[complement]]
                    
# 왜 list 자체를 안 쓰고 dictionaty(Java의 HashMap에 해당)를 쓰느냐?
# -> 리스트는 인덱스 => 값으로 접근, 우리는 값 => 인덱스로 접근할 필요가 있음! 
#    (왜냐, 그 값의 complement가 존재하는지를 따지고 싶으니까. 이렇게 따지면 일일이 다 돌면서 안 찾아도 됨)
#    근데 값을 인덱스로 해서 리스트로 하기엔 부적합!
#    그래서 list 대신 dictionary 사용!
