class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        
        # Step 1: Find the first index i from the right where nums[i] < nums[i+1]
        # (the "pivot" - the rightmost point where the sequence stops being non-increasing)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If such an index exists, find the rightmost element greater than nums[i]
        # to its right, and swap them
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: Reverse the suffix starting at i+1 to get the smallest lexicographic order
        # (the suffix is currently in non-increasing order, so reversing makes it non-decreasing)
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1