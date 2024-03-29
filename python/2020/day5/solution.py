
with open('python\\2020\day5\data.txt') as f:
    lines = f.readlines()

def getRowAndColumn(line):
    row = 0
    column = 0
    #follow directions to split
    first = 0
    last = 127
    for i in range(6):
        difference = last-first
        half = difference//2 + 1
        if line[i] == 'B':
            first += half
        else:
            last -= half
    if line[6] == 'F':
        row = first
    else:
        row = last
    
    right = 0
    left = 7
    for i in range(7, 9):
        difference = left-right
        half = difference//2 + 1
        if line[i] == 'R':
            right += half
        else:
            left -= half
    if line[9] == 'L':
        column = right
    else:
        column = left

    # print(line)
    # print(row, column)
    return row, column

def getSeatId(row, column):
    return row*8 + column

def findMaxSeatId(lines):
    max_seat_id = 0
    for line in lines:
        row, column = getRowAndColumn(line)
        seat_id = getSeatId(row, column)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id

def findMySeat(lines):
    seat_ids = []
    for line in lines:
        row, column = getRowAndColumn(line)
        seat_id = getSeatId(row, column)
        seat_ids.append(seat_id)
    seat_ids.sort()
    stop = False
    i = 0
    while not stop:
        if seat_ids[i] == (seat_ids[i+1] - 1):
            i+=1
        else:
            stop = True
            print('found missing seat', seat_ids[i], seat_ids[i+1])
            return seat_ids[i]+1

    return 0

# print('max seat id is', findMaxSeatId(lines))

print('my seat id is', findMySeat(lines))