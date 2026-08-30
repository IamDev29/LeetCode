class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n1=len(word1)
        n2=len(word2)

        i=0
        j=0

        ans=[]

        while i<n1 and j<n2:
            ans.append(word1[i])
            i+=1
            ans.append(word2[j])
            j+=1

        if i<n1:
            ans.append(word1[i:])
        if j<n2:
            ans.append(word2[j:])

        return "".join(ans)
