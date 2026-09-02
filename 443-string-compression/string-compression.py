class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = []

        ch = chars[0]
        cnt = 1

        for i in range(1, len(chars)):
            if chars[i] == ch:
                cnt += 1
            elif chars[i] != ch and cnt == 1:
                s.append(ch)
                ch = chars[i]
                cnt = 1
            else:
                s.append(ch)
                for c in str(cnt):
                    s.append(c)
                ch = chars[i]
                cnt = 1

        if cnt == 1:
            s.append(ch)
        else:
            s.append(ch)
            for c in str(cnt):
                s.append(c)

        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)