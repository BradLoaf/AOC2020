with open('src.txt', "r") as f:
    lines = f.read().splitlines()

groups = ['']
num_groups = 0
for line in lines:
    if not line:
        groups.append('')
        num_groups += 1
    else:
        groups[num_groups] += (' ' + line)
groups = [group.strip().split() for group in groups]

sum = 0
for group in groups:
    similar = list(group[0])
    for person in group:
        similar = list(set(similar).intersection(set(person)))
    sum += len(similar)
print(sum)