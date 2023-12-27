def part_one(filename):
    oases = load_oasis(filename)
    oases = [list(map(int, line.split(" "))) for line in oases]

    results = []
    for oasis in oases:
        start = oasis[-1]
        vals = []

        while True:
            tmp = []
            i = 0
            size = len(oasis) - 1

            while i < size:
                tmp.append(oasis[i + 1] - oasis[i])
                i += 1

            vals.append(tmp[-1])
            oasis = tmp

            if set(oasis) == {0}:
                break

        results.append(start + sum(vals))
    return sum(results)


def part_two(filename):
    pass


def load_oasis(filename):
    with open(file=filename, mode="r") as f:
        oasis = f.read().splitlines()
    return oasis


if __name__ == "__main__":
    input_path = "./day_09/input.txt"
    print("------Part One-----")
    print(part_one(input_path))

    print("------Part Two-----")
    print(part_two(input_path))
