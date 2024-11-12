import re
with open('src.txt', "r") as f:
    lines = f.read().splitlines()
lines = [[part.strip() for part in line.split(':')] for line in lines]
count = 0
for line in lines:
    key = line[0][::-1][0]
    rule = [int(x) for x in line[0].split()[0].split('-')]
    number = len(re.findall(key, line[1]))
    if number >= rule[0] and number <= rule[1]:
        count+=1
print(count) 