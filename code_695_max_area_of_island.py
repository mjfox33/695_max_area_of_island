class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited_cells = set()
        row_count = len(grid)
        col_count = len(grid[0]) # we are assuming the grid is square
        
        def get_area(row, col):
            if not (0 <= row < row_count and 0 <= col < col_count
                and (row, col) not in visited_cells and grid[row][col]):
                return 0

            visited_cells.add((row, col))
            return (1 + get_area(row+1, col) + get_area(row-1,col) + get_area(row, col+1) + get_area(row, col-1))
        
        return max(get_area(row, col) for row in range(row_count) for col in range(col_count))
