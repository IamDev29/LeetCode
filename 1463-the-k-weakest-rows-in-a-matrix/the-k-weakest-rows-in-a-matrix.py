import heapq
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        heap=[]
        arr=[]
        ans=[]

        for row in mat:
            count=0
            for i in row:
                if i==1:
                    count+=1

            arr.append(count)

        for i,s in enumerate(arr):
            heapq.heappush(heap,(s,i))

        
        for i in range(k):
            _,idx=heapq.heappop(heap)
            ans.append(idx)
        return ans

        

        