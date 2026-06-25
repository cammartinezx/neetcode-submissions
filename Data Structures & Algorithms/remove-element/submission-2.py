class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        #Pointer i: Iterates through the array from left to right
        #Pointer k: Tracks the elements that are not val
        #val is the element to be removed
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k

       