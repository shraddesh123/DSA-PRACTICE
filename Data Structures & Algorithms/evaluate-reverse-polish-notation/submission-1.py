class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for word in tokens:
            if word == "+":
                stack.append(stack.pop() + stack.pop())
            elif word == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif word == "*":
                stack.append(stack.pop() * stack.pop())
            elif word == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(word))

        return stack[0]