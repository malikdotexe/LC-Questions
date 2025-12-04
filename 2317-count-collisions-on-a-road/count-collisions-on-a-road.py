class Solution:
    def countCollisions(self, directions: str) -> int:
        # remove leading L's and trailing R's
        directions = directions.lstrip('L').rstrip('R')
        # all remaining R or L will cause collisions
        return len(directions) - directions.count('S')