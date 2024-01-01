from functools import cache


@cache
def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in cfg else 1

    result = 0

    if cfg[0] in ".?":
        result += count(cfg[1:], nums)

    if cfg[0] in "#?":
        if (
            nums[0] <= len(cfg)
            and "." not in cfg[: nums[0]]
            and (nums[0] == len(cfg) or cfg[nums[0]] != "#")
        ):
            result += count(cfg[nums[0] + 1 :], nums[1:])

    return result


def part_one(filename):
    springs = load_springs(filename)
    total = 0

    for spring in springs:
        cfg, nums = spring.split()
        nums = tuple(
            map(int, nums.split(","))
        )  # a tuple will not be mutated during recursion since it's passed by value

        total += count(cfg, nums)

    return total


def part_two(filename):
    springs = load_springs(filename)
    total = 0

    for spring in springs:
        cfg, nums = spring.split()
        cfg = "?".join([cfg] * 5)
        nums = tuple(map(int, nums.split(",")))
        nums *= 5
        total += count(cfg, nums)

    return total


def load_springs(filename):
    with open(file=filename, mode="r") as f:
        arrangements = f.read().splitlines()
    return arrangements


if __name__ == "__main__":
    input_path = "./day_12/input.txt"
    print("------Part One-----")
    print(part_one(input_path))

    print("------Part Two-----")
    print(part_two(input_path))
