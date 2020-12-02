# I'm just going to brute force this

TARGET_SUM = 2020

def get_numbers_from_file(filename):
    numbers = []
    with open(filename) as file:
        numbers = [int(num) for num in file]

    return numbers


def get_2020_sum_pairs():
    num_list = get_numbers_from_file("input.txt")

    # We loop through the list of numbers and see if the matching
    # second number which sums to 2020 exists in that list
    # If it does, we return the pair of numbers
    # Also, we are assuming that numbers are unique in the list
    for first_num in num_list:
        second_num = TARGET_SUM - first_num

        if second_num in num_list:
            print(f'Solution 1: {first_num}, {second_num}')
            return (first_num, second_num)

    return None

def get_2020_sum_triads():
    num_list = get_numbers_from_file("input.txt")

    for i in range(0, len(num_list)):
        for j in range(1, len(num_list)):
            third_num = TARGET_SUM - num_list[i] - num_list[j]

            if third_num in num_list:
                print(f'Solution 2: {num_list[i]}, {num_list[j]}, {third_num}')
                return (num_list[i], num_list[j], third_num)

    return None


def main():
    pair_tuple = get_2020_sum_pairs()
    print(pair_tuple[0] * pair_tuple[1])

    triad_tuple = get_2020_sum_triads()
    print(triad_tuple[0] * triad_tuple[1] * triad_tuple[2])


if __name__ == "__main__":
    main()
