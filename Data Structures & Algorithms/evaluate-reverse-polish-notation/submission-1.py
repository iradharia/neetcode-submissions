class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["-", "+", "/", "*"]
        for token in tokens:
            if token in operators:
                if token == operators[0]:
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first-second)
                elif token == operators[1]:
                    stack.append(stack.pop() + stack.pop())
                elif token == operators[2]:
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(int(first / second))
                elif token == operators[3]:
                    stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(token))
        return stack[0]