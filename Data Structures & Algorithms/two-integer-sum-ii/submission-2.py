class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #ascending order numbers
        #target = i1,i2 // i1<i2 //i1!=i2
        #no additional space no hashmap
        i1,i2=0,0
        for i,n in enumerate(numbers):
            n2=target-n
            if n2 in numbers[i:]:
                i2= numbers[i:].index(n2)
                return [i+1,i2+i+1]

            


        