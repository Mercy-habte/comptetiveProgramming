class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Index = {n:i for i, n in enumerate(nums1)}
        result = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                index = nums1Index[val]
                result[index] = curr
            if curr in nums1Index:
                stack.append(curr)
        return result

        nums1Index = {n:i for i, n in enumerate(nums1)}
        result = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1Index:
                continue
            for j in range(i+ 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    index = nums1Index[nums2[i]]
                    result[index] = nums2[j]
                    break 
        return result