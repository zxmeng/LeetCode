def sudoku2(grid):
    row = {}
    col = {}

    for i in range(9):
        for j in range(9):
            if grid[i][j] != '.':
                if i not in row:
                    row[i] = [grid[i][j]]
                else:
                    if grid[i][j] in row[i]:
                        return False
                    else:
                        row[i].append(grid[i][j])
                if j not in col:
                    col[j] = [grid[i][j]]
                else:
                    if grid[i][j] in col[j]:
                        return False
                    else:
                        col[j].append(grid[i][j])
    
    for k in range(0,9,3):
        for t in range(0,9,3):
            sub = []
            for i in range(3):
                for j in range(3):
                    if grid[k+i][t+j] != '.':
                        if grid[k+i][t+j] in sub:
                            return False
                        else:
                            sub.append(grid[k+i][t+j])

    # for i in row:
    #     for j in col:
    #         temp = row[i] + col[j]
    #         if len(set(temp)) >= 9:
    #             return False
    
    return True