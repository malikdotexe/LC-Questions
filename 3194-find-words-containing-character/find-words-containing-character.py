class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res=[]
        for i,word in enumerate(words):
            s = set(word)
            if x in s:
                res.append(i)
        return res