import re


def get_values_from_file(filename):
    values = []

    with open(filename) as file:
        values = file.read().splitlines()

    return values


def extract_policy(entry):
    result = re.search("([0-9]+)-([0-9]+) ([a-z]):", entry)
    return (int(result.group(1)), int(result.group(2)), result.group(3))


def extract_password(entry):
    result = re.search(": (.*)", entry)
    return result.group(1)


def is_password_valid_part_one(policy, password):
    min_count     = policy[0]
    max_count     = policy[1]
    required_char = policy[2]

    char_count = password.count(required_char)

    return (char_count >= min_count) and (char_count <= max_count)


def is_password_valid_part_two(policy, password):
    pos_one       = policy[0] - 1
    pos_two       = policy[1] - 1
    required_char = policy[2]

    return (password[pos_one] == required_char) ^ (password[pos_two] == required_char)


def get_number_of_valid_passwords():
    num_valid_passwords_part_one = 0
    num_valid_passwords_part_two = 0
    values = get_values_from_file("input.txt")

    for entry in values:
        policy = extract_policy(entry)
        password = extract_password(entry)

        if is_password_valid_part_one(policy, password):
            num_valid_passwords_part_one += 1

        if is_password_valid_part_two(policy, password):
            num_valid_passwords_part_two += 1

    return (num_valid_passwords_part_one, num_valid_passwords_part_two)


def main():
    num_valid_passwords = get_number_of_valid_passwords()
    print(f'Number of valid passwords part one: {num_valid_passwords[0]}')
    print(f'Number of valid passwords part two: {num_valid_passwords[1]}')


if __name__ == "__main__":
    main()
