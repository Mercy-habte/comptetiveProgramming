class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}

        for i in range (len(nums)):
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]
        
        result = 0
        for key, values in dic.items():
            if len(values)>= 2:
                n = len(values)
                result += n*(n-1) /2
        return int(result)