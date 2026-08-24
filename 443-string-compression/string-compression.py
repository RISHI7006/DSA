class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0  # pointer for writing compressed result
        i = 0      # pointer for reading

        while i < len(chars):
            char = chars[i]
            count = 1

            # Count consecutive occurrences of the current character
            while i + count < len(chars) and chars[i + count] == char:
                count += 1

            # Write the character
            chars[write] = char
            write += 1

            # Write the count if it's more than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            # Move to the next different character
            i += count

        return write