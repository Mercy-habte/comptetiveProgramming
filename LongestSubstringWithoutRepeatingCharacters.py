class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charBucket = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in charBucket:
                charBucket.remove(s[l])
                l+= 1
            charBucket.add(s[r])
            result = max(result, r-l+1)
        return result