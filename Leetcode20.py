class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        bracket_dict = {'(': ')', '{':'}', '[':']'}
        for char in s:
            if len(brackets) == 0:
                brackets.append(char)
                continue
            try:
                if bracket_dict[brackets[-1]] == char:
                    brackets.pop(-1)
                else:
                    brackets.append(char)
            except KeyError:
                return False
        return True if len(brackets) == 0 else False
