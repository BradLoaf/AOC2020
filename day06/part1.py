with open('src.txt', "r") as f:
    lines = f.read().splitlines()

groups = ['']
num_groups = 0
for line in lines:
    if not line:
        groups.append('')
        num_groups += 1
    else:
        groups[num_groups] += line

sum = 0
for group in groups:
    sum += len(set(group))
print(sum)