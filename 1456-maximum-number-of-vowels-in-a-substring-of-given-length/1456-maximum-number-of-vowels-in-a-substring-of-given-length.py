# class Solution:
#     def maxVowels(self, s: str, k: int) -> int:
#         left = 0
#         vowelCount = 0
#         maxVowelCount = 0
        
#         vowels = {'a','e','i','o','u'}

#         for right in range(k):
#             if s[right] in vowels:
#                 vowelCount += 1

#         maxVowelCount = vowelCount

#         while right < len(s)-1:

#             right += 1
#             left += 1

#             if s[right] in vowels:
#                 vowelCount +=1
            
#             if s[left-1] in vowels:
#                 vowelCount -= 1

            
            
#             maxVowelCount = max(vowelCount, maxVowelCount) 
    
#         return maxVowelCount


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        vowelCount = 0
        maxVowelCount = 0

        vowels = {'a', 'e', 'i', 'o', 'u'}

        for right in range(len(s)):

            if s[right] in vowels:
                vowelCount += 1
            
            if (right-left) + 1 > k:

                if s[left] in vowels:
                    vowelCount -= 1

                left += 1
                
            if (right-left) + 1 == k:

                maxVowelCount = max(maxVowelCount, vowelCount)
                
                if maxVowelCount == k:
                    return maxVowelCount

        return maxVowelCount
