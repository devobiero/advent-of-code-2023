import math


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
    steps, nodes = load_maps(filename)
    lookup = dict()

    for node in nodes:
        dirs = node.split(" = ")
        lookup.update({dirs[0]: tuple(dirs[1][1:-1].split(", "))})

    positions = [node for node in lookup if node.endswith("A")]

    cycles = []
    for current in positions:
        cycle = []
        current_steps = steps
        step_count = 0
        first_z = None

        while True:
            while step_count == 0 or not current.endswith("Z"):
                step_count += 1
                current = (
                    lookup.get(current, None)[0]
                    if current_steps[0] == "L"
                    else lookup.get(current, None)[1]
                )
                current_steps = current_steps[1:] + current_steps[0]

            cycle.append(step_count)

            if first_z is None:
                first_z = current
                step_count = 0
            elif current == first_z:
                break

        cycles.append(cycle)

    nums = [cycle[0] for cycle in cycles]
    return math.lcm(*nums)


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
