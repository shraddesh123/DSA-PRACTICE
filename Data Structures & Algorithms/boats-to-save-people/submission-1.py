class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        people=sorted(people)

        i=0
        j=n-1
        res=0
        while i <= j :
            remaining=limit-people[j]
            res+=1
            j-=1
            if i <= j and remaining >= people[i]:
                i+=1

        return res