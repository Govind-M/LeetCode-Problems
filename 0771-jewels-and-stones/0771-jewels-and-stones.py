class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        obj = {}
        count = 0
        
        for i in range(len(jewels)):
            if jewels[i] not in obj:
                obj[jewels[i]] = 1
            else:
                continue

        for j in range(len(stones)):
            if stones[j] in obj:
                count += 1

        return count

