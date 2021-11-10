print("hello world")

numbers = []
with open('python\\2020\day1\data.txt') as f:
    lines = f.readlines()
    for line in lines:
        numbers.append(int(line))

# numbers works
# print(numbers)
'''
part a
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if (numbers[i]+numbers[j] == 2020):
            print("answer:", numbers[i]*numbers[j])
'''

# part b
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        for k in range(j+1,len(numbers)):
            if (numbers[i]+numbers[j]+numbers[k] == 2020):
                print("answer:", numbers[i]*numbers[j]*numbers[k])
