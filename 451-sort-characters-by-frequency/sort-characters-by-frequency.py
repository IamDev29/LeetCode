class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic={}

        for ch in s:
            if ch in dic:
                dic[ch]+=1
            else:
                dic[ch]=1

        
        sorted_items= sorted(dic.items(), key=lambda item: item[1], reverse=True)

        ans=[]

        for key,value in sorted_items:
            ans.append(key*value)

        return "".join(ans)

        