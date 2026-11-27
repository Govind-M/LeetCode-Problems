class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        vowelCount = 0
        maxVowelCount = 0
        
        vowels = {'a','e','i','o','u'}

        for right in range(k):
            if s[right] in vowels:
                vowelCount += 1

        maxVowelCount = vowelCount

        while right < len(s)-1:

            right += 1
            left += 1

            if s[right] in vowels:
                vowelCount +=1
            
            if s[left-1] in vowels:
                vowelCount -= 1

            
            
            maxVowelCount = max(vowelCount, maxVowelCount) 
    
        return maxVowelCount