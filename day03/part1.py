with open('src.txt', "r") as f:
    lines = f.read().splitlines()
count = 0
for step in range(len(lines)):
    if lines[step][step * 3 % len(lines[0])] == '#':
        count += 1

print(count)