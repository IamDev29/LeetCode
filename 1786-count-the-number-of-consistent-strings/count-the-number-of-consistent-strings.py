class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count=0
        include=True
        for word in words:
            for ch in word:
                if ch not in allowed:
                    include=False
                    break
                
            if include:
                count+=1
            else:
                include=True

        
        return count