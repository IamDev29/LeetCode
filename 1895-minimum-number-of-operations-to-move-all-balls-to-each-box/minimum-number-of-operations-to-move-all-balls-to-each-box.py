class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        ans = [0] * n

        # Left to right: contribution from balls on the left
        balls = 0
        moves = 0

        for i in range(n):
            ans[i] += moves

            if boxes[i] == '1':
                balls += 1

            moves += balls

        # Right to left: contribution from balls on the right
        balls = 0
        moves = 0

        for i in range(n - 1, -1, -1):
            ans[i] += moves

            if boxes[i] == '1':
                balls += 1

            moves += balls

        return ans
