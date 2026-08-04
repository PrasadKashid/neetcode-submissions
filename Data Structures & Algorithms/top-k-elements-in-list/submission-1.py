class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        elements = []
        buckets = [[] for _ in range(len(nums) + 1)]

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] not in frequency:
                frequency[nums[i]] = 1
            else:
                frequency[nums[i]] += 1
        for i, n in frequency.items():
            buckets[n].append(i)
        for freq in range(len(buckets) - 1, -1, -1):
            for i in buckets[freq]:
                elements.append(i)
                if len(elements) == k:
                    return elements