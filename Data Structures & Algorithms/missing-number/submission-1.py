class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        out = (n * (n - 1)) // 2
        for num in nums:
            out -= num
        return out
        