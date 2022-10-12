class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        sortedList = sorted(nums)
        dic = {}
        result = []

        for i in range(len(sortedList)):
            if sortedList[i] not in dic:
                dic[sortedList[i]] = i

        for i in nums:
            result.append(dic[i])
        
        return result