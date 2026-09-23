class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        result = strs[0]

        for string in range(len(strs)):
            value = strs[string]
            i = j = 0
            while i < len(value) and j < len(result) and value[i] == result[j]:
                res += value[i]
                i += 1
                j += 1
            result = res
            res=""

        return result
