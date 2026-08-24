class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        arr=address.split('.')
        ans="[.]".join(arr)
        return ans