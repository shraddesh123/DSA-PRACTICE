class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        i=0
        j=n-1
        s=s.lower()
        while i < j :
            if s[i].isalnum() and s[j].isalnum():
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            elif not s[i].isalnum():
                i+=1
            else:
                j-=1
        return True
            

