class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        missing = n*(n+1)//2 - sum(nums)
        return missing