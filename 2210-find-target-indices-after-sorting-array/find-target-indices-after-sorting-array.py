class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        ans=[]

        def fs():
            low=0
            high=len(nums)-1
            first=-1

            while low<=high:

                mid=(low+high)//2

                if nums[mid]==target:
                    first=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1

            return first

                
        def ls():
            low=0
            high=len(nums)-1
            last=-1

            while low<=high:

                mid=(low+high)//2

                if nums[mid]==target:
                    last=mid
                    low=mid+1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1

            return last

        first=fs()
        last=ls()

        if first==-1:
            return ans

        
        for i in range(first,last+1):
            ans.append(i)

        return ans

        
        
        