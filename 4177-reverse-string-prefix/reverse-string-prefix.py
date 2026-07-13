class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        left=0
        right=k-1

        arr=list(s)

        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1

        return "".join(arr)