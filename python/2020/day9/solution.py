
with open('python\\2020\day9\data.txt') as f:
    lines = f.readlines()

# There might be better ways to do this, for now I am happy with an N^2 solution where N=25.
def isSum(target, list):
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if target == list[i]+list[j]:
                return True
    return False


start_size = 25
working_list = []
for i in range(start_size):
    working_list.append(int(lines.pop(0)))

stop = False
while not stop:
    if len(lines) == 0:
        stop = True
        break

    if not isSum(int(lines[0]), working_list):
        print(int(lines[0]), "is not a sum of previous set")
        stop = True
        break

    # set up list for next run
    working_list.pop(0)
    working_list.append(int(lines.pop(0)))

print("the end: part 1")