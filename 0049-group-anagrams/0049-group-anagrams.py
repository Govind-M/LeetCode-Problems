class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # anagrammap = {}

        # for word in strs:
        #     sorted_key = "".join(sorted(word))
        #     if sorted_key not in anagrammap:
        #         anagrammap[sorted_key] = []
        #     anagrammap[sorted_key].append(word)

        
        # return list(anagrammap.values())


        anagrammap = {}

        for word in strs:

            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            count_key = tuple(count)
            
            if count_key not in anagrammap:
                anagrammap[count_key] = []

            anagrammap[count_key].append(word)

        
        return list(anagrammap.values())

            
            

                
