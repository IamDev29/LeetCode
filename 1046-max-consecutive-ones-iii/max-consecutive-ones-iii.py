class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxlen=0
        left=0
        right=0
        numZero=0
        while right<len(nums):
            if nums[right]==0:
                    numZero+=1
            if numZero<=k:
                l=right-left+1
                maxlen=max(maxlen,l)
            while numZero>k:
                if nums[left]==0:
                    numZero-=1
                left+=1
            right+=1

        return maxlen
            
