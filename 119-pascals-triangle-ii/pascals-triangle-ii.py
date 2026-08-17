class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]

        for i in range(1, rowIndex + 1):
            row.append(0)  # extend with a 0 to make space for the new element

            # Update backwards to avoid overwriting values we still need
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j - 1]

        return row
        