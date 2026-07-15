class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        dic={}

        for i in range(len(cards)):
            if cards[i] not in dic:
                dic[cards[i]]=[i]
            else:
                dic[cards[i]].append(i)
        ans=float('inf')
        for key,value in dic.items():
            if len(value)>1:
                for i in range(1,len(value)):
                    ans=min(ans,abs(value[i]-value[i-1])+1)

        if ans==float('inf'):
            return -1
        return ans

        