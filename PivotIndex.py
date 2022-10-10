class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        final = sum(nums)

        leftsum = 0
        for i in range(len(nums)):
            rightsum = final - nums[i] -leftsum
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        return -1