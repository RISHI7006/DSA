class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c ** 0.5)

        while a <= b:
            sq_sum = a * a + b * b

            if sq_sum == c:
                return True
            elif sq_sum < c:
                a += 1  # need a larger sum
            else:
                b -= 1  # need a smaller sum

        return False