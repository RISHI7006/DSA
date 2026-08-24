class Solution:
    def compress(self, chars: list[str]) -> int:
        write = i = 0
        
        while i < len(chars):
            c = chars[i]
            count = 0
            
            while i < len(chars) and chars[i] == c:
                count += 1
                i += 1
            
            chars[write] = c
            write += 1
            
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write