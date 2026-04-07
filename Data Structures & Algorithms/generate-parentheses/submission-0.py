class Solution:
    def generateParenthesis(self, n):
        # your code goes here
        ans = []
        self.generate(0, 0, n, "", ans)
        return ans

    def generate(self, openL, closeL, n, current, ans):

        if openL == closeL == n:
            ans.append(current)
            return

        if openL < n:
            self.generate(openL + 1, closeL, n, current + "(", ans)

        if closeL < openL:
            self.generate(openL, closeL + 1, n, current + ")", ans)
