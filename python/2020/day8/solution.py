import copy

with open('python\\2020\day8\data.txt') as f:
    lines = f.readlines()

def findAccAtStop(lines):
    stop = False
    visited_lines = dict()
    value = 0
    pointer = 0
    while not stop:
        op = lines[pointer].split()[0]
        input = lines[pointer].split()[1]
        if op == 'nop':
            visited_lines[pointer] = 1
            pointer += 1
        elif op == 'acc':
            visited_lines[pointer] = 1
            pointer += 1
            value += int(input)
        elif op == 'jmp':
            visited_lines[pointer] = 1
            pointer += int(input)
        else:
            stop = True
            # print("error, wrong op", op)
            return None, False
        if pointer in visited_lines:
            stop = True
            # print("value:", value)
            return value, False
        if pointer == len(lines):
            stop = True
            # print("reached the end", value)
            return value, True

original_copy = copy.deepcopy(lines)
working_copy = copy.deepcopy(original_copy)

print(findAccAtStop(lines))

for i in range(len(working_copy)):
    if working_copy[i].find('nop') >=0:
        working_copy[i] = working_copy[i].replace('nop', 'jmp')
        value, end = findAccAtStop(working_copy)
        if end:
            print("found end:", value)
        working_copy[i] = working_copy[i].replace('jmp', 'nop')
    if working_copy[i].find('jmp') >= 0:
        working_copy[i] = working_copy[i].replace('jmp', 'nop')
        value, end = findAccAtStop(working_copy)
        if end:
            print("found end:", value)
            print("line changed:", i, working_copy[i])
        working_copy[i] = working_copy[i].replace('nop', 'jmp')