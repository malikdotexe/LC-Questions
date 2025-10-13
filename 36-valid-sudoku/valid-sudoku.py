from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        subbox = defaultdict(list)
        for r in range(len(board)):
            for c in range(len(board[0])):
                curr = board[r][c]
                if curr == ".":
                    continue
                elif curr in row[r] or curr in col[c] or curr in subbox[r//3,c//3]:
                    return False
                else:
                    row[r].append(curr)
                    col[c].append(curr)
                    subbox[r//3,c//3].append(curr)
        return True


