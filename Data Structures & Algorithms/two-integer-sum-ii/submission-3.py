class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,n in enumerate(numbers):
            n2=target-n
            for i2 in range(i, len(numbers)):
                if numbers[i2]==n2:
                    return [i+1,i2+1]
        