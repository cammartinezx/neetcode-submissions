class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_recursive(nums,target,0,len(nums)-1)
    
    def binary_recursive(self, arr: List[int],target: int,left: int,right: int):
        #left mid and right are index
        if left>right:
            return -1
        mid= (left+right)//2
        if arr[mid]== target:
            return mid
        elif arr[mid]<target:
            return self.binary_recursive(arr,target,mid+1,right)
        elif arr[mid]>target:
            return self.binary_recursive(arr,target,left,mid-1)