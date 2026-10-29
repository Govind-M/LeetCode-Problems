class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = {}
        def fn(remWord):

            if remWord in dp:
                return dp[remWord]

            res = False

            if remWord == "" :
                return True

            for i in range(len(remWord)):
                subWord = remWord[:i+1]
                if subWord in wordDict and fn(remWord[i+1:]):
                    res = True
                    break
                dp[remWord] = res
            return res
    
        return fn(s)