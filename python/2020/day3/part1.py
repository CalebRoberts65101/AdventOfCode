
with open('python\\2020\day3\data.txt') as f:
    lines = f.readlines()

## start in the top left, 0,0
lay = 0
hang = 0

# found by counting data
width = 30

lay_d = 3
hang_d = 1

tree_hits = 0
stop = False
# loop for part 1
stop = True
while not stop:
    if hang == len(lines):
        stop = True
        continue
    # figure out if we colide
    if lines[hang][lay] == '#':
        print(hang, lay)
        print(lines[hang])
        tree_hits+=1
    # increment
    lay = (lay+lay_d) % (width+1)
    hang = hang+hang_d

# print("tree hits:", tree_hits)

def tree_loop(lines, lay_d, hang_d):
    lay = 0
    hang = 0
    tree_hits = 0
    stop = False
    while not stop:
        if hang >= len(lines):
            stop = True
            continue
        # figure out if we colide
        if lines[hang][lay] == '#':
            print(hang, lay)
            print(lines[hang])
            tree_hits+=1
        # increment
        lay = (lay+lay_d) % (width+1)
        hang = hang+hang_d

    return tree_hits

result_1 = tree_loop(lines, 1, 1)
result_2 = tree_loop(lines, 3, 1)
result_3 = tree_loop(lines, 5, 1)
result_4 = tree_loop(lines, 7, 1)
result_5 = tree_loop(lines, 1, 2)

print("results:", result_1, result_2, result_3, result_4, result_5)
print("answer:", result_1 * result_2 * result_3 * result_4 * result_5)