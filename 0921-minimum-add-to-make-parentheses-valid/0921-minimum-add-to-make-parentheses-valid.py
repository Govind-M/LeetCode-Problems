class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # stack = []
        # count = 0

        # for ch in s:
        #     if ch == "(":
        #         stack.append(ch)
        #         count += 1
        #     elif len(stack) > 0:
        #         stack.pop()
        #         count -= 1
        #     else:
        #         count +=1
        

        # return count


        oCount = 0
        cCount = 0

        for ch in s:
            if ch == "(":
                oCount += 1
            else:
                oCount -= 1
                if oCount < 0:
                    oCount = 0
                    cCount +=1

        return oCount + cCount
