with open('src.txt', "r") as f:
    lines = f.read().splitlines()

essential_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passports = ['']
num_passport = 0
for line in lines:
    if not line:
        passports.append('')
        num_passport += 1
    else:
        passports[num_passport] += (' ' + line)

passports = [passport.strip().split() for passport in passports]
count = 0
for passport in passports:
    passport_dict = {field[0]:field[1] for field in [item.split(':') for item in passport]}
    valid = True
    for field in essential_fields:
        if field not in passport_dict:
            valid = False
    if valid:
        count += 1

print(count)