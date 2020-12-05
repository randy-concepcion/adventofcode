# Trash brute-force code
# NOTE: There's a bug in here
import re


REQUIRED_FIELDS = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def get_values_from_file(filename):
    values = None
    with open(filename) as file:
        values = file.read()

    return values.split("\n\n")


def get_valid_passports_count_part_one(passports):
    count = 0

    for passport in passports:
        if all(field in passport for field in REQUIRED_FIELDS):
            count += 1

    return count


def is_field_valid(key, value):
    if key == "byr":
        if (int(value) >= 1920) and (int(value) <= 2002):
            return True

    elif key == "iyr":
        if (int(value) >= 2010) and (int(value) <= 2020):
            return True

    elif key == "eyr":
        if (int(value) >= 2020) and (int(value) <= 2030):
            return True

    elif key == "hgt":
        if not ("cm" in value or "in" in value):
            return False

        result = re.search("(\d+)(\w+)", value)

        if result is None:
            return False

        if result.group(2) is None:
            return False

        metric = result.group(2).lower()
        height = int(result.group(1))

        if (metric == "cm" and height >= 150 and height <= 193) or \
            (metric == "in" and height >= 59 and height <= 76):
            return True

    elif key == "hcl":
        result = re.search("#([\dabcdef]+)", value)

        if result is not None and len(result.group(1)) == 6:
            return True

    elif key == "ecl":
        if value in EYE_COLORS:
            return True

    elif key == "pid":
        if len(value) <= 9 and value.isdigit():
            return True

    elif key == "cid":
        return True

    return False


def get_valid_passports_count_part_two(passports):
    count = 0

    valid_flag = True
    for passport in passports:
        if not all(field in passport for field in REQUIRED_FIELDS):
            continue

        # Split by whitespace
        fields = passport.split()

        for field in fields:
            key_value = field.split(":")

            if not is_field_valid(key_value[0], key_value[1]):
                valid_flag = False

        if valid_flag:
            count += 1
        else:
            valid_flag = True

    return count


def main():
    passports = get_values_from_file("input.txt")
    valid_count_one = get_valid_passports_count_part_one(passports)

    print(f'Number of valid passports for part one: {valid_count_one}')

    valid_count_two = get_valid_passports_count_part_two(passports)
    print(f'Number of valid passports for part two: {valid_count_two}')


if __name__ == "__main__":
    main()
