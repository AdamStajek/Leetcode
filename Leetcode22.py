class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
       stack = []
       valids = []
       def gen(countO, countC):
            if countO == countC == n:
               valids.append("".join(stack))
               return
            if countO < n:
                stack.append('(')
                gen(countO + 1, countC)
                stack.pop()
            if countO > countC:
                stack.append(')')
                gen(countO, countC + 1)
                stack.pop()
       gen(0,0)
       return valids