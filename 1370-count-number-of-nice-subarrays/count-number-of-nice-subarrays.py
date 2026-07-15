class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic={0:1}
        sumi=0
        count=0

        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
            
            sumi+=nums[i]
            if sumi-k in dic:
                count+=dic[sumi-k]
            
            if sumi in dic:
                dic[sumi]+=1
            else:
                dic[sumi]=1

            

        return count

        
