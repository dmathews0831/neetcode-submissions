class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_circle(nums) -> int:
            cache = {}

            def rob(i) -> int:
                if i >= len(nums):
                    return 0
                if i in cache:
                    return cache[i]
                cache[i] = max((nums[i] + rob(i+2)), rob(i+1))
                return cache[i]

            return max(rob(0), rob(1))

        return max(rob_circle(nums[:-1]), rob_circle(nums[1:]), nums[0])