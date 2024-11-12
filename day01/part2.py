with open('src.txt', "r") as f:
    lines = f.read().splitlines()
nums = [int(num) for num in lines]
for num1 in nums:
    for num2 in nums:
        for num3 in nums:
            if num1 != num2 and num2 != num3 and num1 != num3 and num1 + num2 + num3 == 2020:
                print(num1 * num2 * num3)