import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #piles, each entry is # of bananas in that pile
        #h hours for each pile
        #if pile[i]< k finished eating in 1 hr
        #if pile[i]< k
        l,r= 1,max(piles)
        while l<=r:
            k= (l+r)//2
            total = self.getTotal(piles,k)
            if total > h:
                l= k+1
            else:
                r = k-1
                ans=k
        return ans


    def getTotal(self,piles: List[int], k: int) -> int:
        total = 0
        for i in range(len(piles)):
            if piles[i]>k:
                total+=math.ceil(piles[i]/k)
            else:
                total+=1
        return total
        