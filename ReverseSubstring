class Solution:
    def reverseParentheses(self, s: str) -> str:
       
            ans = []
            for c in s:
                if c == ')':
                    t = []
                    while ans[-1] != '(':
                        t.append(ans.pop())
                    ans.pop()
                    ans = ans + t
                else:
                    ans.append(c)
            return "".join(ans)