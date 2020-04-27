class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keyIsValueDict = dict()
        
        for i in range(0, len(nums)):
            complement = target - nums[i]
            
            if keyIsValueDict.get(complement) != None:
                if nums[i] > complement :
                    return [keyIsValueDict[complement], i]
                else :
                    return [i, keyIsValueDict[complement]]
            
            keyIsValueDict[nums[i]] = i
 
 # 얘는 넣기 전에 dictionary 안에 complement 있는지 확인!!
 # 그러면 일단 solution 2 처럼 자기 자신 확인하는 조건식 쓸 필요없음! -> 넣을 때마다 바로바로 확인하기 떄문!
 # 헷갈렸던 점 : 4 4 와 같은 경우는 어떡함? -> solution 2로는 저거 잡을 수 없! 
 # (왜냐면, dictionary에 'dict_이름[이전 키 값(value)] = 새로운 값(list index)' 이렇게 쓰면 새로운 값(list index)으로 바뀌기 때문!!)
 # 그러나 solution 3에서는 이런 거 잡아낼 수 있!!, 따라서 더 좋은 방법!
