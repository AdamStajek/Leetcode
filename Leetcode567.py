class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters = Counter(s1)

        for i in range(len(s2)):
            if s2[i] in letters:
                letters[s2[i]] -= 1
            if i >= len(s1) and s2[i - len(s1)] in letters:
                letters[s2[i - len(s1)]] += 1

            if all(letters[i] == 0 for i in letters):
                return True
        return False



