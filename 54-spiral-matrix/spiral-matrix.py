class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Optional: handle empty matrix
        if not matrix or not matrix[0]:
            return []

        m = len(matrix)
        n = len(matrix[0])

        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        ans = []

        while top <= bottom and left <= right:

            # 1. top row: left -> right
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # 2. right column: top -> bottom
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # 3. bottom row: right -> left (if any rows remain)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # 4. left column: bottom -> top (if any cols remain)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans