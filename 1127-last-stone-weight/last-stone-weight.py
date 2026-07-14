import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in range(len(stones)):
            stones[i]=-stones[i]

        heapq.heapify(stones)

        while len(stones)>1:
            a=-heapq.heappop(stones)
            b=-heapq.heappop(stones)

            if a!=b:
                heapq.heappush(stones,-(a-b))

        if len(stones)==0:
            return 0
        return -stones[0]

        