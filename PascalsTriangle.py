'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:



Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]
'''


def generate(self, numRows: int) -> List[List[int]]:
    result = [[1]]
    for i in range(1, numRows):
        row = []
        for j in range(i + 1):
            prev = result[-1]
            left = prev[j - 1] if j - 1 >= 0 else 0
            right = prev[j] if j < len(prev) else 0
            row.append(left + right)

        result.append(row)
    return result