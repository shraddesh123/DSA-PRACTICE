class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hashmap = {")": "(", "}": "{", "]": "["}

        for word in s:
            if word in hashmap:

                if stack and hashmap[word] == stack[-1]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(word)
        return True if not stack else False