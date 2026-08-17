class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # If lengths differ, rotation can never work
        if len(s) != len(goal):
            return False

        # All rotations of s appear as substrings in s + s
        return goal in s + s
        