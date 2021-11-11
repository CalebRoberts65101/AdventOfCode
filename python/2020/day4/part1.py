
with open('python\\2020\day4\data.txt') as f:
    all_text = f.read()


chuncks = all_text.split('\n\n')
# print(chuncks)

valid_count = 0
# for each chunck split and check if valid
for text in chuncks:
    parts = text.split()
    print(text)
    print(parts)
    parts_found = 0
    has_cid = False
    invalid = False
    for part in parts:
        parts = part.split(':')
        left = parts[0]
        right = parts[1]
        print(left, right)
        if left == 'ecl':
            print( 'ecl', parts_found)
            valid_eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if right in valid_eye_color:
                parts_found +=1
            else:
                print('invalid eye')
                invalid = True
        elif left == 'pid':
            print( 'pid', parts_found)
            if len(right) == 9:
                parts_found +=1
            else:
                print('invalid pid')
                invalid = True
        elif left == 'eyr':
            print( 'eyr', parts_found)
            if len(right) == 4 and (int(right) >= 2020 and int(right) <= 2030):
                parts_found +=1
            else:
                print('invalid eyr')
                invalid = True
        elif left == 'hcl':
            print( 'hcl', parts_found)
            valid = True
            valid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
            valid = valid and right[0] == '#'
            valid = valid and right[1] in valid_chars
            valid = valid and right[2] in valid_chars
            valid = valid and right[3] in valid_chars
            valid = valid and right[4] in valid_chars
            valid = valid and right[5] in valid_chars
            valid = valid and right[6] in valid_chars
            if valid:
                parts_found += 1
            else:
                print('invalid hcl')
                invalid = True
        elif left == 'byr':
            print( 'byr', parts_found)
            if len(right) == 4 and (int(right) >= 1920 and int(right) <= 2002):
                parts_found +=1
            else:
                print('invalid byr')
                invalid = True
        elif left == 'iyr':
            print( 'iyr', parts_found)
            if len(right) == 4 and (int(right) >= 2010 and int(right) <= 2020):
                parts_found +=1
            else:
                print('invalid iyr')
                invalid = True
        elif left == 'cid':
            has_cid = True
        elif left == 'hgt':
            print('hgt', parts_found)
            num = right[:-2]
            unit = right[-2:]
            if unit == 'cm':
                if int(num) >= 150 and int(num) <=193:
                    parts_found +=1
                else:
                    print('invalid cm')
                    invalid = True
            elif unit == 'in':
                if int(num) >= 59 and int(num) <= 76:
                    parts_found +=1
                else:
                    print('invalid cm')
                    invalid = True
            else:
                print('invalid unit')
                invalid = True
        
    print(parts_found, invalid)
    if parts_found == 7 and not invalid: 
        valid_count+=1
    


print("valid passports:", valid_count)
# end part 1

