class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maxi=float('-inf')

        if len(arr)==1:
            arr[0]=-1
            return arr

        for i in range(len(arr)-1,-1,-1):
            if i==len(arr)-1:
                maxi=max(maxi,arr[i])
                arr[i]=-1
            else:
                temp=arr[i]
                arr[i]=maxi
                maxi=max(maxi,temp)

        return arr