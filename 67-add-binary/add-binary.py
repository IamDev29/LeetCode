class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = []
        i = len(a) - 1
        j = len(b) - 1
        carry = '0'

        while i >= 0 and j >= 0:
            if a[i] == '1' and b[j] == '1':
                if carry == '0':
                    ans.append('0')
                    carry = '1'
                else:
                    ans.append('1')
                    carry = '1'

            elif a[i] == '0' and b[j] == '0':
                if carry == '0':
                    ans.append('0')
                    carry = '0'
                else:
                    ans.append('1')
                    carry = '0'

            elif a[i] == '0' and b[j] == '1':
                if carry == '0':
                    ans.append('1')
                    carry = '0'
                else:
                    ans.append('0')
                    carry = '1'

            elif a[i] == '1' and b[j] == '0':
                if carry == '0':
                    ans.append('1')
                    carry = '0'
                else:
                    ans.append('0')
                    carry = '1'

            i -= 1
            j -= 1

        while i >= 0:
            if a[i] == '1':
                if carry == '0':
                    ans.append('1')
                    carry = '0'
                else:
                    ans.append('0')
                    carry = '1'
            else:
                if carry == '0':
                    ans.append('0')
                    carry = '0'
                else:
                    ans.append('1')
                    carry = '0'
            i -= 1

        while j >= 0:
            if b[j] == '1':
                if carry == '0':
                    ans.append('1')
                    carry = '0'
                else:
                    ans.append('0')
                    carry = '1'
            else:
                if carry == '0':
                    ans.append('0')
                    carry = '0'
                else:
                    ans.append('1')
                    carry = '0'
            j -= 1

        if carry == '1':
            ans.append('1')

        return "".join(ans[::-1])