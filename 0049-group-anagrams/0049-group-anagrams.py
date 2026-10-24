class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        anagrammap = {}

        for word in strs:
            sorted_key = "".join(sorted(word))
            if sorted_key not in anagrammap:
                anagrammap[sorted_key] = []
            anagrammap[sorted_key].append(word)

        
        return list(anagrammap.values())
                
