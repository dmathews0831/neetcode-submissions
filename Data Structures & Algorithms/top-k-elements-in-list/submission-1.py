class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        return [tup[0] for tup in counts[:k]]
