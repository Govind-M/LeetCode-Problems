class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dic = {}
    
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in dic or dic[t[j]] == 0:
                return False
            else:
                dic[t[j]] -= 1
        
        return True
        

