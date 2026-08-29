class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}
        stack = []  # monotonic decreasing stack

        for num in nums2:
            # While current num is greater than the stack's top,
            # we've found the "next greater element" for that top
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        # Elements remaining in the stack have no next greater element
        # (they're implicitly -1 via .get() default)

        return [next_greater.get(num, -1) for num in nums1]
        