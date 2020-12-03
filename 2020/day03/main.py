def get_map_section_from_file(filename):
    map_section = []
    with open(filename) as file:
        map_section = file.read().splitlines()

    return map_section


def get_number_of_trees(slope_x, slope_y):
    MAP_SECTION = get_map_section_from_file("input.txt")
    MAP_WIDTH = len(MAP_SECTION[0])
    MAP_HEIGHT = len(MAP_SECTION)

    x = 0
    trees_count = 0
    for y in range(0, MAP_HEIGHT - 1, slope_y):
        # Navigate the map section
        y += slope_y
        x += slope_x

        # Did x exceed MAP_WIDTH?
        if x >= MAP_WIDTH:
            x -= MAP_WIDTH

        # Check where we landed
        check_char = MAP_SECTION[y][x]
        if check_char == "#":
            trees_count += 1

    return trees_count

def main():
    num_trees1 = get_number_of_trees(1, 1)
    num_trees2 = get_number_of_trees(3, 1)
    num_trees3 = get_number_of_trees(5, 1)
    num_trees4 = get_number_of_trees(7, 1)
    num_trees5 = get_number_of_trees(1, 2)
    print(f'Number of trees1: {num_trees1}')
    print(f'Number of trees2: {num_trees2}')
    print(f'Number of trees3: {num_trees3}')
    print(f'Number of trees4: {num_trees4}')
    print(f'Number of trees5: {num_trees5}')

    product = num_trees1 * num_trees2 * num_trees3 * num_trees4 * num_trees5
    print(f'Product of all trees: {product}')

if __name__ == "__main__":
    main()
