class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        left = right=max_len=max_freq=0
        while right < len(s):
            if s[right] not in dic:
                dic[s[right]] = 1
            else:
                dic[s[right]] += 1
            max_freq = max(max_freq, dic[s[right]])
            if (right - left + 1) - max_freq > k:
                dic[s[left]] -= 1
                left += 1
            else:
                max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
