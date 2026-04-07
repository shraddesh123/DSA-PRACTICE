class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        for i in s1:
            s1_freq[i] = 1 + s1_freq.get(i, 0)

        k = len(s1)
        i = j = 0
        s2_freq = {}

        while j < len(s2):

            s2_freq[s2[j]] = s2_freq.get(s2[j], 0) + 1

            if j - i + 1 < k:
                j += 1
                

            elif s1_freq == s2_freq:
                return True
            
            else:

                s2_freq[s2[i]] -= 1
                if s2_freq[s2[i]] == 0:
                    del s2_freq[s2[i]]
                i += 1
                j += 1

        return False
             