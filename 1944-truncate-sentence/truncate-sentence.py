class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        arr=s.split(" ")
        ans=arr[:k]

        string=" ".join(ans)

        return string
        