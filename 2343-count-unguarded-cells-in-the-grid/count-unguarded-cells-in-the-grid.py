class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        
        walls = set(map(tuple, walls))
        guards = set(map(tuple, guards))
        
        for r, c in guards:
            # mark left
            for j in range(c - 1, -1, -1):
                if (r, j) in walls or (r, j) in guards:
                    break
                matrix[r][j] = 1
            
            # mark right
            for j in range(c + 1, n):
                if (r, j) in walls or (r, j) in guards:
                    break
                matrix[r][j] = 1
            
            # mark up
            for i in range(r - 1, -1, -1):
                if (i, c) in walls or (i, c) in guards:
                    break
                matrix[i][c] = 1
            
            # mark down
            for i in range(r + 1, m):
                if (i, c) in walls or (i, c) in guards:
                    break
                matrix[i][c] = 1
        
        # mark guards & walls as 1(non-empty)
        for r, c in guards:
            matrix[r][c] = 1
        for r, c in walls:
            matrix[r][c] = 1
        
        # return unguarded (still 0)
        return sum(row.count(0) for row in matrix)
