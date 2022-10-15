class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum = 0

        for i in range(k):
            sum += arr[i]
        
        cutoff = threshold * k
        result = int(sum >= cutoff)
        for start in range(k, len(arr)):
            sum += arr[start]
            sum -= arr[start-k]
            if sum >= cutoff:
                result += 1

        return result