class Solution:
    def maxArea(self, heights: List[int]) -> int:
        out = 0
        for l in range(len(heights)):
            r = len(heights) - 1
            while l < r:
                if (heights[l] * (r-l)) < out:
                    break
                out = max(out, min(heights[l], heights[r])*(r-l))
                r -= 1
        return out
