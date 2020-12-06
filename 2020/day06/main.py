def get_values_from_file(filename):
    values = []

    with open(filename) as file:
        values = file.read()

    return values.split("\n\n")


def sum_counts():
    answers_list = get_values_from_file("input.txt")

    count = 0
    for group in answers_list:
        answers = group.rstrip().split("\n")
        unique_answers = set(''.join(answers))

        count += len(unique_answers)

    return count

def main():
    count = sum_counts()
    print(f"Sum of counts: {count}")


if __name__ == "__main__":
    main()
