class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
        out = []
        for i in counts:
            if k == 0:
                return out
            k -= 1
            out.append(i)
        return out
