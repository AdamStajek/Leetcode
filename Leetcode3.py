class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substr = 0
        left = 0
        letters = set()

        for right in range(len(s)):
            while s[right] in letters:
                letters.discard(s[left])
                left += 1
            letters.add(s[right])
            max_substr = max(max_substr, right - left + 1)
        return max_substr


