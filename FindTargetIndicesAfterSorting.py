class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []

        for i, x in enumerate(nums):
            if x == target:
                result.append(i)
        
        return result