class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans=0

        for i in range(len(s)-1,-1,-1):
            if i==len(s)-1:
                ans+=roman_values[s[i]]
            elif roman_values[s[i]]<roman_values[s[i+1]]:
                ans-=roman_values[s[i]]
            else:
                ans+=roman_values[s[i]]

        return ans
        