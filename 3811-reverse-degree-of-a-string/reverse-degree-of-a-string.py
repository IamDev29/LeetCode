class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        sumi=0
        i=1

        for ch in s:
            reverse=ord('z')-ord(ch)+1
            sumi+=(reverse*i)
            i+=1
        
        return sumi
            


        