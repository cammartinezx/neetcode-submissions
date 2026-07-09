class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i = target - j and j = target - i so 
        #iterate through list
        #if I store j then when is time to get the diff(j) from target - i  then j will be in the map
        #the key is to store the values from the list and if I find the diff =value then return
        #more efficient than array because to look for a value is O(1)
        hashMap = {}

        for i,x in enumerate(nums):
            diff = target - x
            if diff in hashMap:
                return [hashMap[diff],i]
            hashMap[x]=i 


        