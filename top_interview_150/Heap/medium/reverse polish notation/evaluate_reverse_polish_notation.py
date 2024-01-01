class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []
        operators = "+-*/"

        for token in tokens:
            if token in operators:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if token == "+":
                    sol = operand2 + operand1
                elif token == "-":
                    sol = operand2 - operand1
                elif token == "*":
                    sol = operand2 * operand1
                elif token == "/":
                    sol = operand2 / operand1
                stack.append(int(sol))
            else:
                stack.append(int(token))

        return stack[0]