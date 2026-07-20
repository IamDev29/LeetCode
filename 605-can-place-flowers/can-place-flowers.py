class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count=0

        if len(flowerbed)==1:
            if n<=1 and flowerbed[0]==0:
                return True
            elif n==0 and flowerbed[0]==1:
                return True
            else:
                return False

        for i in range(len(flowerbed)):
            if i==0:
                if flowerbed[i]==0 and flowerbed[i+1]==0:
                    count+=1
                    flowerbed[i]=1
            elif i==len(flowerbed)-1:
                if flowerbed[i]==0 and flowerbed[i-1]==0:
                    count+=1
                    flowerbed[i]=1
            else:
                if flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0:
                    count+=1
                    flowerbed[i]=1
            
            if count>=n:
                return True

        return False


