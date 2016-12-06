def moveLeft(grid):
    final_grid = []
    for row in grid:
        for i in range(0,3):
            row = pushLeft(row)
            if row[i] == row[i+1]:
                row[i] = str(int(row[i]) * 2)
                row[i+1] = '0'
            row = pushLeft(row)
        final_grid.append((' '.join(map(str, row))))
    return final_grid;

def pushLeft(temp):
    row =[]
    for i in temp:
        row.append(i)

    for run in range(0, 4):
        for i in range(0 , 3):
            if row[i] == '0':
                row[i] = row[i+1]
                row[i+1] = '0'
    return row

def pushRight(temp):
    row = []
    for i in temp:
        row.append(i)

    for run in range(0, 4):
        for i in range(3 , 0, -1):
            if row[i] == '0':
                row[i] = row[i-1]
                row[i-1] = '0'
    return row

def moveRight(grid):
    final_grid = []
    for row in grid:
        for i in range(3, 0, -1):
            row = pushRight(row)
            if row[i] == row[i-1]:
                row[i] = str(int(row[i]) * 2)
                row[i-1] = '0'
            row = pushRight(row)
        final_grid.append((' '.join(map(str, row))))
    return final_grid;

def moveUp(grid):
    rotated = zip(*grid[::-1])
    rotated = moveRight(rotated)
    i = 0
    for row in rotated:
        rotated[i] = row.split(' ')
        i+=1
    temp = zip(*rotated[::-1])
    temp = zip(*temp[::-1])
    final = zip(*temp[::-1])
    i=0
    for row in final:
        final[i] = (' '.join(map(str, row)))
        i+=1
    return final

def moveDown(grid):
    rotated = zip(*grid[::-1])
    rotated = moveLeft(rotated)
    i = 0
    for row in rotated:
        rotated[i] = row.split(' ')
        i+=1
    temp = zip(*rotated[::-1])
    temp = zip(*temp[::-1])
    final = zip(*temp[::-1])
    i=0
    for row in final:
        final[i] = (' '.join(map(str, row)))
        i+=1

    return final

row1 = raw_input().split(" ")
row2 = raw_input().split(" ")
row3 = raw_input().split(" ")
row4 = raw_input().split(" ")
thegrid = (row1, row2, row3, row4)


direction = int(raw_input())

if direction == 0:
    for row in moveLeft(thegrid):
        print(row)
elif direction == 1:
    for row in moveUp(thegrid):
        print(row)
elif direction == 2:
    for row in moveRight(thegrid):
        print(row)
elif direction == 3:
    for row in moveDown(thegrid):
        print(row)
