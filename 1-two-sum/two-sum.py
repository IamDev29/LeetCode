class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic={}

        for i in range(len(nums)):
            sol=target-nums[i]
            if sol in dic:
                return [i,dic[sol]]
            else:
                dic[nums[i]]=i