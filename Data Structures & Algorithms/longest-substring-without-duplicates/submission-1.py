class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        maximum=0
        i=j=0
        window=set()
        while j < n:
            
            while s[j] in window:
                window.remove(s[i])
                i+=1
            
            window.add(s[j])
            maximum=max(maximum,j-i+1)
            j+=1
                
            
        return maximum