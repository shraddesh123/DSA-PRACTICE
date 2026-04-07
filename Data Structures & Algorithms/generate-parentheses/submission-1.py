class Solution:
    def generateParenthesis(self, n):
        # your code goes here
        stack=[]
        ans = []


        def generate(openL,closeL):

            if openL == closeL == n:
                ans.append("".join(stack))
                return

            if openL < n:
                stack.append("(")
                generate(openL+1,closeL)
                stack.pop()

            if closeL < openL:
                stack.append(")")
                generate(openL,closeL+1)
                stack.pop()
        generate(0,0)
        return ans