with open('src.txt', "r") as f:
    lines = f.read().splitlines()
count1, count2, count3, count4, count5 = 0, 0, 0, 0, 0
for step in range(len(lines)):
    if lines[step][step % len(lines[0])] == '#':
        count1 += 1
    if lines[step][step * 3 % len(lines[0])] == '#':
        count2 += 1
    if lines[step][step * 5 % len(lines[0])] == '#':
        count3 += 1
    if lines[step][step * 7 % len(lines[0])] == '#':
        count4 += 1
    if step * 2 < len(lines) and lines[step * 2][step % len(lines[0])] == '#':
        count5 += 1

print(count1 * count2 * count3 * count4 * count5)