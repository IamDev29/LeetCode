class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        ans=[]

        for word in words:
            total=0

            for ch in word:
                index=ord(ch)-ord('a')
                total+=weights[index]
            
            value=total%26
            ans.append(chr(ord('z')-value))

        return ''.join(ans)
        