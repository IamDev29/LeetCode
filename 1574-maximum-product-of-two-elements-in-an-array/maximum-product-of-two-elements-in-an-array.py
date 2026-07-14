import heapq
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        heap=[-x for x in nums]

        heapq.heapify(heap)
        

        a=-(heapq.heappop(heap))-1
        
        b=-(heapq.heappop(heap))-1

        return a*b

        