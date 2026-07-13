class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=-1

        dic={}

        for i in range(len(nums)):
            if nums[i]%2==0:
                if nums[i] in dic:
                    dic[nums[i]]+=1
                else:
                    dic[nums[i]]=1

        for num in nums:
            if num%2==0:
                if dic[num]==1:
                    return num

        return ans
        