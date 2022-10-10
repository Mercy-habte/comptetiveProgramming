class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_container = {"}":"{","]":"[",")":"("}
        opening_bracets = set(["(","[","{"])

        for x in s:
            if x in opening_bracets:
                stack.append(x)
            elif stack and stack[-1] == bracket_container[x]:
                stack.pop()
            else:
                return False

        if stack:
            return False
        else:
            return True