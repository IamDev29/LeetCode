class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):

            if (
                r<0 or
                c<0 or
                r>=rows or
                c>=cols or
                grid[r][c]==0
            ):
                return 1
            
            
            return 0


        ans = 0

        for i in range(rows):

            for j in range(cols):

                if grid[i][j]==1:

                    ans+=dfs(i+1,j)
                    ans+=dfs(i-1,j)
                    ans+=dfs(i,j+1)
                    ans+=dfs(i,j-1)
                    

                

        return ans
        