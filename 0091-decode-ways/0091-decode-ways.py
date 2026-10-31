class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = {}
        def fn(remS):

            if remS == '':
                return 1


            if remS in dp:
                return dp[remS]


            oneDigit = remS[len(remS)-1:]
            twoDigit = remS[len(remS)-2:] if len(remS) >= 2 else ""

            ans = 0

            if oneDigit !="0":
                ans += fn(remS[:len(remS)-1])
            if len(twoDigit) == 2 and "10" <= twoDigit <="26":
                ans += fn(remS[:len(remS)-2])

            dp[remS] = ans
            return ans

        return fn(s)