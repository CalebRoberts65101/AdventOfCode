import copy

with open('python\\2020\day11\data.txt') as f:
    my_lines = f.readlines()

with open('python\\2020\day11\given.txt') as f:
    pass
    # my_lines = f.readlines()

# print(lines)

grid = []

for line in my_lines:
    new_line = []
    for char in line:
        if char != '\n':
            new_line.append(char)
    grid.append(new_line)



# print(grid)

def inGrid(grid, x, y):
    if x < 0 or y < 0:
        return False
    if x < len(grid):
        if y < len(grid[x]):
            return True
    return False

def countAdjacentFull(grid, x, y):
    count = 0
    if inGrid(grid,x+1,y+1):
        if grid[x+1][y+1] == '#':
            count+=1
    if inGrid(grid,x+1,y):
        if grid[x+1][y] == '#':
            count+=1
    if inGrid(grid,x+1,y-1):
        if grid[x+1][y-1] == '#':
            count+=1
    if inGrid(grid,x,y+1):
        if grid[x][y+1] == '#':
            count+=1
    if inGrid(grid,x,y-1):
        if grid[x][y-1] == '#':
            count+=1
    if inGrid(grid,x-1,y+1):
        if grid[x-1][y+1] == '#':
            count+=1
    if inGrid(grid,x-1,y):
        if grid[x-1][y] == '#':
            count+=1
    if inGrid(grid,x-1,y-1):
        if grid[x-1][y-1] == '#':
            count+=1
    return count

def countSeenFull(grid, x, y):
    count = 0
    directions = [(1,-1), (1,0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
    for dx,dy in directions:
        stop = False
        cx = x +dx
        cy = y + dy
        while not stop:
            if inGrid(grid, cx, cy):
                if grid[cx][cy] == '.':
                    cx += dx
                    cy += dy
                elif grid[cx][cy] == 'L':
                    stop = True
                elif grid[cx][cy] == '#':
                    stop = True
                    count += 1
            else:
                stop = True
    return count

# for line in grid:
    # print(line)

num_rounds = 0
grid_changed = True
while grid_changed:
    grid_changed = False
    next_grid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                if countSeenFull(grid, i, j) >= 5:
                    grid_changed = True
                    next_grid[i][j] = 'L'
            if grid[i][j] == 'L':
                if countSeenFull(grid, i, j) == 0:
                    grid_changed = True
                    next_grid[i][j] = '#'
    grid = next_grid
    print("round:", num_rounds)
    num_rounds+=1

for line in grid:
    pass
    # print(line)
count = 0
for line in grid:
    for char in line:
        if char == '#':
            count += 1
print("full seats", count)