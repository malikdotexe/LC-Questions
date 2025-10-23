from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramset = defaultdict(list)
        for word in strs:
            frequencyarray = [0]*26
            for letter in word:
                frequencyarray[ord(letter)-ord("a")]+=1
            anagramset[tuple(frequencyarray)].append(word)
        return list(anagramset.values())
