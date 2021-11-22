
with open('python\\2020\day13\data.txt') as f:
    lines = f.readlines()

'''
my_depart_time = int(lines[0])
all_buses = lines[1]
buses = []
for time in all_buses.split(','):
    if time == 'x':
        pass
    else:
        buses.append(int(time))

best_time = 100 * my_depart_time
best_bus = 0

for bus in buses:
    current = 0
    while current < my_depart_time:
        current+=bus
    if current < best_time:
        best_time = current
        best_bus = bus

print("answer:", (best_time-my_depart_time) * best_bus)
'''

# part 2

# build requirements
reqs = []
counter = 0
for i in lines[1].split(','):
    if i != 'x':
        reqs.append((int(i), counter))
    counter+=1

print(reqs)

# find number such that
# ax1 = bx2-y2 = cx3-y3 = dx4-y4 ...

# one method, find how often first set occurs bc it should be periodic, from that set, at each additional constraint
# find a*13 = b*41 - 3
# I don't have the math to do that well

# second method
# try each "stop" for a number, see if the reqs work
# valid if counter = axN + yN

stop = False
counter = 0
# to allow a quicker start for the problem, its given that counter > 100000000000000
counter = (100017320000000//641)*641
print(counter)
tmp = reqs[0]
reqs[0] = reqs[2]
reqs[2] = tmp
while not stop: 
    # step counter
    counter+= reqs[0][0]
    dirty = False
    counter -= 13
    for req in reqs:
        if (counter + req[1])%req[0] == 0:
            continue
        else:
            dirty = True
            break
    if not dirty:
        print("found timestop:", counter)
        stop = True
    counter += 13

    if counter%(reqs[0][0]*10000000) == 0:
        print('hit number', counter)

# 13, 41, 641, 19, 17, 29, 661, 37, 23

