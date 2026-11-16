class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        maxlen = 0
        currlen = 0
        included = {}


        while j < len(s):
            if s[j] in included and included[s[j]] >= i:
                i = included[s[j]] + 1

            included[s[j]] = j
            currlen = (j-i) + 1
            maxlen = max(maxlen, currlen)  
            j += 1

        return maxlen
