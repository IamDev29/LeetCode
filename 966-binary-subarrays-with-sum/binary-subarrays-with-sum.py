class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        dic={0:1}
        sumi=0
        count=0

        for i in range(len(nums)):
            
            
            sumi+=nums[i]
            if sumi-goal in dic:
                count+=dic[sumi-goal]
            
            if sumi in dic:
                dic[sumi]+=1
            else:
                dic[sumi]=1

            

        return count
        