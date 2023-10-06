class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for word in strs:
            letters = sorted(word)
            letters = "".join(letters)
            if letters in hm:
                hm[letters].append(word)
            else:
                hm[letters] = [word]
        
    
        
        return list(hm.values())
