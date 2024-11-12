with open('src.txt', "r") as f:
    lines = f.read().splitlines()
nums = [int(num) for num in lines]
diff = {}
for num in nums:
    if diff.get(num, 0) + num == 2020:
        print(diff.get(num) * num)
    else:
        diff[2020 - num] = num