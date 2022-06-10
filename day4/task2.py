import re
import os
valid_passports = 0
passport_no = 0
with open(os.path.join(os.getcwd(), 'input.txt')) as f:
    lines = f.readlines()
    new_lines = [rmv_newline.replace('\n','') for rmv_newline in lines]


    joined_str = [' '.join(new_lines)]
    no_newlines = [new_str.replace('\n','') for new_str in joined_str]

    no_spaces = [rmv_spaces.split('  ') for rmv_spaces in no_newlines][0]

    list_of_ids = [passport.split(' ') for passport in no_spaces]
    for passport in list_of_ids:
        met_requirements = 0
        valid_entries = 0
        passport_no += 1
        for entry in passport:

            if entry[0:3]=='byr':
                valid_entries += 1
                if 1919 < int(entry[4:]) and int(entry[4:]) < 2003 and len(entry[4:]) == 4:
                    met_requirements += 1

            if entry[0:3]=='iyr':
                valid_entries += 1
                if 2009 < int(entry[4:]) and int(entry[4:]) < 2021 and len(entry[4:]) == 4:
                    met_requirements += 1

            if entry[0:3]=='eyr':
                valid_entries += 1
                if 2019 < int(entry[4:]) and int(entry[4:]) < 2031 and len(entry[4:]) == 4:
                    met_requirements += 1

            if entry[0:3]=='hgt':
                valid_entries += 1
                if entry[-2:]=='cm':
                    if 149 < int(entry[4:-2]) and int(entry[4:-2]) < 194:
                        met_requirements += 1

                elif entry[-2:]=='in':
                    if 58 < int(entry[4:-2]) and int(entry[4:-2]) < 77:
                        met_requirements += 1

            if entry[0:3]=='hcl':
                valid_entries += 1
                if entry[4]=='#' and re.match('[0-9a-f]{6}', entry[5:]) is not None and len(entry[5:])==6:
                    met_requirements += 1

            if entry[0:3]=='ecl':
                valid_entries += 1
                if entry[4:] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and len(entry[4:]) == 3:
                    met_requirements += 1

            if entry[0:3]=='pid':
                valid_entries += 1
                if re.match('[0-9]{9}', entry[4:]) is not None and len(entry[4:])==9:
                    met_requirements += 1

        if met_requirements == 7:
            valid_passports += 1

print(valid_passports)



