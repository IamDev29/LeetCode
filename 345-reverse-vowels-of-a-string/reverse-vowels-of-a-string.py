class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=list(s)
        left=0
        right=len(arr)-1

        vowels=['a','e','i','o','u']

        while left<right:
            if arr[left].lower() in vowels and arr[right].lower() in vowels:
                arr[left],arr[right]=arr[right],arr[left]
                left+=1
                right-=1

            elif arr[left].lower() in vowels and arr[right].lower() not in vowels:
                right-=1
            elif arr[left].lower() not in vowels and arr[right].lower() in vowels:
                left+=1
            else:
                left+=1
                right-=1

        return "".join(arr)


        