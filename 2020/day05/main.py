def get_values_from_file(filename):
    values = []

    with open(filename) as file:
        values = file.read().splitlines()

    return values


def get_row(seat_code):
    # Only get first 7 characters
    row_chars = seat_code[0:7]

    # Convert to binary string
    binary = row_chars.replace("F", "0").replace("B", "1")

    return int(binary, 2)


def get_column(seat_code):
    # Only get last 3 characters
    col_chars = seat_code[7:10]

    # Convert to binary string
    binary = col_chars.replace("R", "1").replace("L", "0")

    return int(binary, 2)


def get_highest_seat_id():
    seat_list = (get_values_from_file("input.txt"))

    highest_seat_id = 0
    for seat in seat_list:
        row_num = get_row(seat)
        col_num = get_column(seat)

        seat_id = row_num * 8 + col_num

        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    return highest_seat_id


def get_my_seat():
    seat_list = (get_values_from_file("input.txt"))
    valid_seat_list = []

    for seat in seat_list:
        row_num = get_row(seat)

        if row_num == 0 or row_num == 127:
            continue

        col_num = get_column(seat)

        seat_id = row_num * 8 + col_num
        valid_seat_list.append(seat_id)

    valid_seat_list.sort()

    for i in range(0, len(valid_seat_list) - 1):
        if (valid_seat_list[i] + 1) != valid_seat_list[i+1]:
            return valid_seat_list[i] + 1

    return 0


def main():
    highest_seat_id = get_highest_seat_id()
    print(f'Highest seat ID: {highest_seat_id}')

    my_seat_id = get_my_seat()
    print(f'My seat ID: {my_seat_id}')


if __name__ == "__main__":
    main()
