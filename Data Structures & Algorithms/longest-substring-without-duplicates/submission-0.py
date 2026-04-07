class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        maximum=0
        i=j=0
        window=set()
        while j < n:
            
            if s[j]not in window:
                window.add(s[j])
                maximum=max(maximum,j-i+1)
                j+=1
                
            elif s[j] in window:
                window.remove(s[i])
                i+=1
        return maximum