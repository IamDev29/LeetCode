class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n=len(boxes)

        arr=[]
        
        for i in range(n):
            if boxes[i]=='1':
                arr.append(i)

        ans=[]
        for i in range(n):
            step=0
            for num in arr:
                step+=abs(i-num)
            ans.append(step)

        return ans
            

