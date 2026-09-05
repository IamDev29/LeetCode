class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        counts = [row.count('1') for row in bank if row.count('1') > 0]
    
        ans = 0
        for i in range(len(counts) - 1):
            ans += counts[i] * counts[i + 1]
        
        return ans
        