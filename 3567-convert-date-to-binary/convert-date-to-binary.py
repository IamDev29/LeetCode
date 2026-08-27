class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        arr=date.split('-')
        ans=[]

        for i in arr:
            ans.append(bin(int(i))[2:])

        x="-".join(ans)
        return x