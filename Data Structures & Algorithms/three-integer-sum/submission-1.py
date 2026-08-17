class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        out = []
        nums = sorted(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            const = nums[i]
            l, r = i + 1, len(nums)-1
            while l < r:
                num = const + nums[l] + nums[r]
                if num > 0:
                    r -= 1
                elif num < 0:
                    l += 1
                else:
                    out.append([const, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return out
