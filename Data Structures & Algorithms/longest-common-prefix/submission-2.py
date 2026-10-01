class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        first=strs[0]

        

        for char in range(len(strs)):
            word=strs[char]
            i=j=0
            while i <len(word) and j < len(first) and word[i]==first[j]:
                res+=word[i]
                i+=1
                j+=1
            first=res
            res=""
        return first    