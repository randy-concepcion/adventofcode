SLOPE_X = 3
SLOPE_Y = 1


def get_map_section_from_file(filename):
    map_section = []
    with open(filename) as file:
        map_section = file.read().splitlines()

    return map_section


def get_number_of_trees():
    MAP_SECTION = get_map_section_from_file("input.txt")
    MAP_WIDTH = len(MAP_SECTION[0])
    MAP_HEIGHT = len(MAP_SECTION)

    x = 0
    trees_count = 0
    for y in range(0, MAP_HEIGHT - 1):
        # Navigate the map section
        y += SLOPE_Y
        x += SLOPE_X

        # Did x exceed MAP_WIDTH?
        if x >= MAP_WIDTH:
            x -= MAP_WIDTH

        # Check where we landed
        check_char = MAP_SECTION[y][x]
        if check_char == "#":
            trees_count += 1

    return trees_count

def main():
    num_trees = get_number_of_trees()
    print(f'Number of trees: {num_trees}')

if __name__ == "__main__":
    main()
