def get_values_from_file(filename):
    values = []

    with open(filename) as file:
        values = file.read()

    return values.split("\n\n")


def sum_counts_one():
    answers_list = get_values_from_file("input.txt")

    count = 0
    for group in answers_list:
        answers = group.rstrip().split("\n")
        unique_answers = set(''.join(answers))

        count += len(unique_answers)

    return count

def sum_counts_two():
    answers_list = get_values_from_file("input.txt")

    count = 0
    for group in answers_list:
        answers = group.rstrip().split("\n")

        if len(answers) == 1:
            count += len(set(answers[0]))

        else:
            set_list = []
            for ans in answers:
                set_list.append(set(ans))

            count += len(set.intersection(*set_list))

    return count

def main():
    count_one = sum_counts_one()
    print(f"Sum of counts one: {count_one}")

    count_two = sum_counts_two()
    print(f"Sum of counts two: {count_two}")


if __name__ == "__main__":
    main()
