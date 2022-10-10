class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        currentsum = 0
        prefixsum = { 0:1 }

        for n in nums:
            currentsum += n
            diff = currentsum -k

            result += prefixsum.get(diff,0)
            prefixsum[currentsum] = 1+prefixsum.get(currentsum,0)

        return result
       