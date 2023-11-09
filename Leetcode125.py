class Solution:
    def isPalindrome(self, s: str) -> bool:
        punctuations = """!()-[]{};:'`"\,<>./?@#$%^&*_~ """
        valid_string = [i.lower() for i in s if i not in punctuations]
        left = 0
        right = len(valid_string) - 1
        while(right > left):
            if valid_string[left] != valid_string[right]:
                return False
            left += 1
            right -= 1
        return True