
with open('python\\2020\day6\data.txt') as f:
    lines = f.read()

chuncks = lines.split('\n\n')

# part 1
total_count = 0
for chunck in chuncks:
    group_count = 0
    found_letters = dict()
    people = chunck.split('\n')
    for person in people:
        for char in person:
            if char not in found_letters:
                group_count += 1
                total_count += 1
                found_letters[char] = 1
    # print("group count: ",group_count)

# print("total count:", total_count)

#part 2
total_count = 0
for chunck in chuncks:
    group_count = 0
    found_letters = dict()
    people = chunck.split('\n')
    for person in people:
        for char in person:
            if char not in found_letters:
                found_letters[char] = 1
            else:
                found_letters[char] += 1
    for key, value in found_letters.items():
        if value == len(people):
            group_count+=1
            total_count+=1
    print(group_count)

print('total count:', total_count)


