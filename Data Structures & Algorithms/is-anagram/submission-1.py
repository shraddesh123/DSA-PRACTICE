class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def dic(d):
            hash={}
            for i in range(len(d)):
                if d[i] in hash:
                    hash[d[i]]+=1
                else:
                    hash[d[i]]=1
            return hash

        first=dic(s)
        second=dic(t)
        return first==second
