class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        seen = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for i in range(len(sentence)):

            if sentence[i] not in seen:
                seen[sentence[i]] = 1

        for i in range(len(alphabet)):

            if alphabet[i] not in seen:
                return False

        
        return True
            
        