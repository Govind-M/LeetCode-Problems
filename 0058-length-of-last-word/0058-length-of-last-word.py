class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newtext = s.split()
        return len(newtext[len(newtext) -1])