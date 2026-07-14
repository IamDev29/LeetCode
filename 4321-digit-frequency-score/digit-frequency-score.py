class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0

        s=str(n)

        dic={}
        
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

        for s,i in dic.items():
            count+= int(s)*i

        return count
        