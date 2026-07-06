class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic={0:1}
        sumi=0
        cnt=0

        for i in range(len(nums)):
            

            sumi+=nums[i]

            target=sumi-k
            if target in dic:
                cnt+=dic[target]
            
            if sumi in dic:
                dic[sumi]+=1
            else:
                dic[sumi]=1
            

        return cnt

        