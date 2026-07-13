import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total=1
        zeros=[]
        n = len(nums)
        if nums:
            for i in range(n):
                if nums[i]!=0:
                    total=total*nums[i]
                else:
                    zeros.append(i)
                    if len(zeros)>1:
                        return [0]*n

        
            if zeros:
                nums = [0]*n
                for i in zeros:
                    nums[i]=total
                return nums
            else:
                for i in range(n):
                    nums[i]=int(total/nums[i])
        return nums
        