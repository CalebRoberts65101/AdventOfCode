
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
target = 0
while not stop:
    if len(lines) == 0:
        stop = True
        break

    if not isSum(int(lines[0]), working_list):
        print(int(lines[0]), "is not a sum of previous set")
        target = int(lines[0])
        stop = True
        break

    # set up list for next run
    working_list.pop(0)
    working_list.append(int(lines.pop(0)))

print("the end: part 1")


with open('python\\2020\day9\data.txt') as f:
    lines = f.readlines()

nums = []
for line in lines:
    nums.append(int(line))

def findSumFirstAndLast(target, nums):
    for i in range(len(nums)-1):
        sum = nums[i]
        for j in range(i+1, len(nums)):
            sum += nums[j]
            if sum == target:
                print("found result")
                return i,j
            # exit early since all nums are positive
            if sum >= target:
                break

print(findSumFirstAndLast(target, nums))
# maunally see results and [ab]use min and max to get a simple answer
print(min(nums[562:578]) + max(nums[562:578]))