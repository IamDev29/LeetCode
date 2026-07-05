class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left=0
        right=1

        ans=[0]*len(nums)

        for num in nums:
            if num>0:
                ans[left]=num
                left+=2
            else:
                ans[right]=num
                right+=2

        return ans

        
        