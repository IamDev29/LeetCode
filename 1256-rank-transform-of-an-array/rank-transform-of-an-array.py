class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        nums=sorted(arr)

        dic={}
        i=1
        for num in nums:
            if num not in dic:
                dic[num]=i
                i+=1

        ans=[]

        for a in arr:
            ans.append(dic[a])

        return ans

        