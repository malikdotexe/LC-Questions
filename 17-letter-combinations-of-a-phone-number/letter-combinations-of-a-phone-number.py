class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #edge case
        if not digits:
            return []
        digitdict = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
        res= []
        temp = []
        def dfs(i):
            #base case with return
            if len(temp)==len(digits):
                res.append("".join(temp))
                return 
            # pick each possible letter for the current digit and explore
            for ch in digitdict[digits[i]]:
                temp.append(ch)    # choose this letter
                dfs(i + 1)         # move to the next digit
                temp.pop()         # remove the letter to backtrack
        dfs(0)
        return res


