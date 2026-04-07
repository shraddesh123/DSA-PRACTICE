class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        first=strs[0]

        for string in range(len(strs)):
            i=j=0
            value=strs[string]
            while i < len(value) and j < len(first) and value[i]==first[j]:
                res+= first[j]
                i+=1
                j+=1
            first = res
            res=""
        return first



        
