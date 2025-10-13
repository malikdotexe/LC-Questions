class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack =[]
        res = []
        for word in words:
            count = Counter(word)
            if stack and stack[-1]== count:
                continue
            else:
                res.append(word)
                stack.append(count)
        return res