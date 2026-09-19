class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # handle k >= n (rotating by n is a no-op)
        
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        # Step 1: reverse the entire array
        reverse(0, n - 1)
        # Step 2: reverse the first k elements
        reverse(0, k - 1)
        # Step 3: reverse the remaining n-k elements
        reverse(k, n - 1)