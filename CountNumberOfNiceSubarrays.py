class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count, countOdd, prefix =0, 0 , collections.defaultdict(int)
        for i in range(len(nums)):
            prefix[countOdd] +=1

            if nums[i] % 2:
                countOdd += 1

            if countOdd >= k:
                countPossibleSubarrayStart = countOdd - k 
                count += prefix[countPossibleSubarrayStart]
        
        return count