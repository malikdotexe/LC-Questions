from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0 
        def bfs(point):
            [r,c] = point
            q = deque([[r,c]])
            visited.add((r, c))
            #The direction list helps us easily go in all 4 directions without hardcoding. By adding its elements to our coordinates, we can generate coordinates for the cell up/down/left/right.
            direction = [[0,1],[1,0],[0,-1],[-1,0]]
            while q:
                for i in range(len(q)):
                    [r,c] = q.popleft()
                    for d in direction:
                        #nr is newrow and similarly nc
                        nr = r+d[0]
                        nc = c+d[1]
                        #checking that new coordinates dont go out of bounds , cell is 1 and not already visited
                        if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="1" and (nr,nc) not in visited:
                            q.append([nr,nc])
                            visited.add((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]=="1":
                    bfs([r,c])
                    count+=1

        return count