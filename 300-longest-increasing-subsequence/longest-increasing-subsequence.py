class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []  # tails[i] = smallest possible tail value of an increasing subsequence of length i+1
        
        for num in nums:
            # Binary search for the leftmost position where num can replace/extend
            lo, hi = 0, len(tails)
            while lo < hi:
                mid = (lo + hi) // 2
                if tails[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid
            
            if lo == len(tails):
                tails.append(num)  # num extends the longest subsequence found so far
            else:
                tails[lo] = num    # num replaces an element to keep tails as small as possible
        
        return len(tails)