def DFS(i, j, grid, visited):
    row = len(grid)
    col = len(grid[0])
    if -1 < i < row and -1 < j < col:
        if grid[i][j] == 0:
            return 0, visited
        elif visited[i][j] == 1:
            return 0, visited
        else:
            count = 1
            visited[i][j] = 1
            count_t, visited = DFS(i-1, j-1, grid, visited)
            count += count_t
            count_t, visited = DFS(i-1, j, grid, visited)
            count += count_t
            count_t, visited = DFS(i-1, j+1, grid, visited)
            count += count_t
            count_t, visited = DFS(i, j-1, grid, visited)
            count += count_t
            count_t, visited = DFS(i, j+1, grid, visited)
            count += count_t
            count_t, visited = DFS(i+1, j-1, grid, visited)
            count += count_t
            count_t, visited = DFS(i+1, j, grid, visited)
            count += count_t
            count_t, visited = DFS(i+1, j+1, grid, visited) 
            count += count_t
            return count, visited
    else:
        return 0, visited

def get_biggest_region(grid):
    biggest = 0
    row = len(grid)
    col = len(grid[0])
    
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                visited = [[0] * col for x in range(row)]
                count, _ = DFS(i, j, grid, visited)
                biggest = max(biggest, count)
    return biggest
    

n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)
