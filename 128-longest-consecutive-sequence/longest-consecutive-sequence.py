class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        nums_set=set(nums)
        longest=1

        for num in nums_set:
            if num-1 not in nums_set:
                cnt=1
                while num+1 in nums_set:
                    cnt+=1
                    num=num+1

                longest=max(longest,cnt)

        return longest

        