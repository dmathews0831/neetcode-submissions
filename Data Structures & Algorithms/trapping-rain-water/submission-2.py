class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        out = 0
        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                out += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                out += rightMax - height[r]
        return out