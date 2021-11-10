
with open('python\\2020\day2\data.txt') as f:
    lines = f.readlines()

good_passwords = 0
for line in lines:
    parts = line.split(' ')
    counts = parts[0].split('-')
    min_count = int(counts[0])
    max_count = int(counts[1])
    letter = parts[1][0]
    password = parts[2]
    '''
    print(line)
    print(left_position)
    print(right_position)
    print(letter)
    print(password)
    '''
    if (min_count <= password.count(letter) <= max_count):
        good_passwords+=1

print("number of good passwords:", good_passwords)

# part 2
good_passwords = 0
for line in lines:
    parts = line.split(' ')
    positions = parts[0].split('-')
    left_position = int(positions[0])
    right_position = int(positions[1])
    letter = parts[1][0]
    password = parts[2]
    '''
    print(line)
    print(left_position)
    print(right_position)
    print(letter)
    print(password)
    '''
    if (password[left_position-1] == letter or password[right_position-1] == letter) and not (password[left_position-1] == letter and password[right_position-1] == letter):
        good_passwords+=1
