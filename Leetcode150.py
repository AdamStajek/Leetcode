class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        pointer = 0
        while pointer != len(tokens):
            if tokens[pointer] == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif tokens[pointer] == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif tokens[pointer] == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            elif tokens[pointer] == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a * b))
            else:
                stack.append(int(tokens[pointer]))
            pointer += 1
        return int(stack[-1])


