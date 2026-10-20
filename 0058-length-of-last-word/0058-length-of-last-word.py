class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0

        for n in range(len(s) - 1, -1, -1):
            if s[n] != " ":
                count += 1
            elif s[n] == " " and count>0:
                break

            

        return count

