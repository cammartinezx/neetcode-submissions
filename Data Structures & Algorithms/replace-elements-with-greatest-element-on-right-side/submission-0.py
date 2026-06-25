class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        k= pos=0
        for i in range(len(arr)-1):
            if pos<=i:
                nex=arr[pos+1:]
                print(nex,pos,i)

                k=max(arr[pos+1:])
                pos=arr.index(k)
            arr[i]=k
        arr[-1]=-1
        return arr


        
        
        
        
        
        """k= pos=0
        for i in range(len(arr)):
            if pos<=i:
                nex=arr[pos+1:]
                print(nex,pos,i)

                k=max(arr[pos+1:])
                pos=arr.index(k)
            arr[i]=k
        arr[-1]=-1"""



        