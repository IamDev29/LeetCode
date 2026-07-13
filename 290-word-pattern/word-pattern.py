class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dic1={}
        dic2={}

        arr=s.split(" ")
        if len(pattern)!=len(arr):
            return False

        for i in range(len(arr)):
            if pattern[i] in dic1 and dic1[pattern[i]]!=arr[i]:
                return False
            
            if arr[i] in dic2 and dic2[arr[i]]!=pattern[i]:
                return False

            dic1[pattern[i]]=arr[i]
            dic2[arr[i]]=pattern[i]

        return True


        