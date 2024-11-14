with open('src.txt', "r") as f:
    lines = f.read().splitlines()

ids = []
for line in lines:
    low, high = 0, 127
    for letter in line[:7]:
        mid = (high - low) // 2 + low
        if letter == 'F':
            high = mid
        else:
            low = mid + 1
    row = low

    low, high = 0, 7
    for letter in line[7:]:
        mid = (high - low) // 2 + low
        if letter == 'L':
            high = mid
        else:
            low = mid + 1
    col = low

    ids.append(row * 8 + col)

print(max(ids))