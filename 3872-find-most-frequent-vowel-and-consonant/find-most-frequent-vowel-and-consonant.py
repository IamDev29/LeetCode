class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowel_dict = {}
        consonant_dict = {}
        
        vowels = "aeiou"
        
        for ch in s:
            if ch in vowels:
                vowel_dict[ch] = vowel_dict.get(ch, 0) + 1
            else:
                consonant_dict[ch] = consonant_dict.get(ch, 0) + 1
        
        max_vowel = 0
        max_consonant = 0
        
        if vowel_dict:
            max_vowel = max(vowel_dict.values())
        
        if consonant_dict:
            max_consonant = max(consonant_dict.values())
        
        return max_vowel + max_consonant