class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        neg=False
        ans=[]

        for i in range(len(s)):
            if i==0 and s[i]=="-":
                neg=True
            elif i==0 and s[i]=="+":
                neg=False
            
            elif s[i].isdigit():
                ans.append(s[i])
            else:
                break

        num="".join(ans)
        if num=="":
            return 0

        num=int(num)

        if neg:
            num=-num

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
        


        


        
        