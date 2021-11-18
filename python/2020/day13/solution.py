
with open('python\\2020\day13\data.txt') as f:
    lines = f.readlines()

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
