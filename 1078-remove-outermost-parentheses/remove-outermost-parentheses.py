class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0   # count of '(' in current primitive
        right = 0  # count of ')' in current primitive
        
        # stk will store characters of current primitive
        stk = []
        # ans will store final result
        ans = []
        
        for ch in s:
            # start of a new primitive
            if left == right:
                # we are about to start a new primitive with an '('
                # push it to stack but DO NOT add to result (this is outer '(')
                stk = []        # reset stack for new primitive
                left = 0
                right = 0

            # update counters and push to primitive stack
            if ch == '(':
                left += 1
                stk.append(ch)
            else:  # ch == ')'
                right += 1
                stk.append(ch)

            # if primitive finished (balanced)
            if left == right and left != 0:
                # stk now contains full primitive, e.g. "(())()"
                # remove outermost pair: skip first and last char
                # inner = stk[1:-1]
                ans.extend(stk[1:-1])
                # next loop iteration will see left==right and treat as new primitive
        
        return "".join(ans)