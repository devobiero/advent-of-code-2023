def part_one(filename):
    steps, nodes = load_maps(filename)
    lookup = dict()

    for node in nodes:
        dirs = node.split(" = ")
        lookup.update({dirs[0]: tuple(dirs[1][1:-1].split(", "))})

    node = "AAA"
    count = 0

    while node != "ZZZ":
        for step in steps:
            count += 1
            node = (
                lookup.get(node, None)[0] if step == "L" else lookup.get(node, None)[1]
            )

    return count


def part_two(filename):
    pass


def load_maps(filename):
    with open(file=filename, mode="r") as f:
        steps, _, *nodes = f.read().splitlines()
    return steps, nodes


if __name__ == "__main__":
    input_path = "./day_08/input.txt"
    print("------Part One-----")
    print(part_one(input_path))

    print("------Part Two-----")
    print(part_two(input_path))
