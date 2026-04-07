class Solution:
    def validPalindrome(self, s: str) -> bool:
        n= len(s)

        i=0
        j=n-1

        while i < j:
            if s[i]!=s[j]:
                sLeft=s[i+1:j+1]
                sRight=s[i:j]

                return(sLeft==sLeft[::-1]or sRight==sRight[::-1])
            i+=1
            j-=1
        return True
