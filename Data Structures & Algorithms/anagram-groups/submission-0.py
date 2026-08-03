class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        grouped_values = {}
        for i in range(len(strs)):
            freq = [0] * 26

            for ch in strs[i]:
                freq[ord(ch) - ord('a')] += 1

            key = tuple(freq)
            if key not in grouped_values:
                grouped_values[key] = []

            grouped_values[key].append(strs[i])
        return list(grouped_values.values())