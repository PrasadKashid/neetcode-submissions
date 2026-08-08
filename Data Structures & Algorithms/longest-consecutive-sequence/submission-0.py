class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        maxLength = 0

        for num in numsSet:
            if num - 1 not in numsSet:
                current_length = 1
                current_number = num

                while current_number + 1 in numsSet:
                    current_number += 1
                    current_length += 1

                maxLength = max(maxLength, current_length)
        return maxLength