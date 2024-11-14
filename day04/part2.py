with open('src.txt', "r") as f:
    lines = f.read().splitlines()

passports = ['']
valid_eyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
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
    valid = 0
    for key, value in passport_dict.items():
        print(valid)
        match key:
            case 'byr':
                if int(value) <= 2002 and int(value) >= 1920:
                    valid += 1
            case 'iyr':
                if int(value) <= 2020 and int(value) >= 2010:
                    valid += 1
            case 'eyr':
                if int(value) <= 2030 and int(value) >= 2020:
                    valid += 1
            case 'hgt':
                if value[::-1][:2] == 'ni' and value[:2].isdigit():
                    if int(value[:2]) >= 59 and int(value[:2]) <= 76:
                        valid += 1
                if value[::-1][:2] == 'mc' and value[:3].isdigit():
                    if int(value[:3]) >= 150 and int(value[:3]) <= 193:
                        valid += 1
            case 'hcl':
                if (value[0] == '#') and len(value) == 7:
                    valid += 1
            case 'ecl':
                if value in valid_eyes:
                    valid += 1
            case 'pid':
                if len(value) == 9:
                    valid += 1
        print(key, value)
    if valid >= 7:
        count += 1

print('proper count', count)