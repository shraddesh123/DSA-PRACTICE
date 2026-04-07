class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        new_s=""
        for i in range(n):
            if s[i].isalnum():
                new_s+= s[i].lower()
        
        i =0
        j = len(new_s)-1

        while i < j :
            if new_s[i]!=new_s[j]:
                return False
            i+=1
            j-=1
        return True

