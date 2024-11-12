with open('src.txt', "r") as f:
    lines = f.read().splitlines()
lines = [[part.strip() for part in line.split(':')] for line in lines]
count = 0
for line in lines:
    key = line[0][::-1][0]
    rule = [int(x) for x in line[0].split()[0].split('-')]
    matches = 0
    if line[1][rule[0] - 1] == key:
        matches += 1
    if line[1][rule[1] - 1] == key:
        matches += 1
    if matches == 1:
        count += 1
print(count) 