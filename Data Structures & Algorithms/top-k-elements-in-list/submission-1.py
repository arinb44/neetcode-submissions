class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        items = sorted(counts.items(), key=lambda p: p[1], reverse=True)
        results = []
        for i in range(k):
            results.append(items[i][0])
        return results