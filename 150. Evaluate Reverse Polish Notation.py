class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        
        for token in tokens:
            if token in operators:
                if token == '+':
                    stack.append(stack.pop() + stack.pop())
                elif token == '-':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2 - num1)
                elif token == '*':
                    stack.append(stack.pop() * stack.pop())
                else:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(int(num2 / num1))
            else:
                stack.append(int(token))
        
        return stack.pop()
