class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # Use array instead of dict/Counter for faster access
        need = [0] * 128
        for char in t:
            need[ord(char)] += 1

        required = sum(1 for count in need if count > 0)

        window = [0] * 128
        formed = 0
        left = 0
        min_len = float('inf')
        min_left = 0

        s_len = len(s)

        for right in range(s_len):
            char_code = ord(s[right])
            window[char_code] += 1

            if need[char_code] > 0 and window[char_code] == need[char_code]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                left_char_code = ord(s[left])
                window[left_char_code] -= 1
                if need[left_char_code] > 0 and window[left_char_code] < need[left_char_code]:
                    formed -= 1

                left += 1

        return "" if min_len == float('inf') else s[min_left:min_left + min_len]