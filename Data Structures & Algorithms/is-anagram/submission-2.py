class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False
        freq = [0] * 26

        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1
        for count in freq:
            if count != 0 :
                return False
        return True

        # SC, TC = o(n)
        # if len(s) != len(t):
        #     return False
        # s_freq = {}
        # t_freq = {}
        
        # for i in s:
        #     if i not in s_freq:
        #         s_freq[i] = 1
        #     else:
        #         s_freq[i] += 1
        # for i in t:
        #     if i not in t_freq:
        #         t_freq[i] = 1
        #     else:
        #         t_freq[i] += 1
        # if(s_freq == t_freq):
        #     return True
        # else:
        #     return False