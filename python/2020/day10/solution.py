
with open('python\\2020\day10\data.txt') as f:
    lines = f.readlines()

data = []
for line in lines:
    data.append(int(line))

data.sort()

print(data)

diffs = [0, 0, 0]
for i in range(len(data)-1):
    if data[i+1] - data[i] == 1:
        diffs[0]+=1
    if data[i+1] - data[i] == 2:
        diffs[1]+=1
    if data[i+1] - data[i] == 3:
        diffs[2]+=1

# plus one because of the inital plug in and for the adaptor
print((diffs[0]+1)*(diffs[2]+1))

# try to count number of arangments (DP yay!)
count_so_far = [0]*len(data)
print(count_so_far)

for i in range(len(data)):
# for i in range(4):
    less_one = 0
    if i - 1 >=0:
        if data[i] - data[i-1] <= 3:
            less_one = count_so_far[i-1]
    less_two = 0
    if i - 2 >=0:
        if data[i] - data[i-2] <= 3:
            less_two = count_so_far[i-2]
    less_three = 0
    if i - 3 >=0:
        if data[i] - data[i-3] <= 3:
            less_three = count_so_far[i-3]
    count_so_far[i] = less_one + less_two + less_three
    if data[i] <= 3: #can connect to base
        count_so_far[i]+=1

print(count_so_far)
print(count_so_far[-1])