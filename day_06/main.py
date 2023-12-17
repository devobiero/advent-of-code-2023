import math


def part_one(filename):
    races = load_races(filename)
    times = [int(time) for time in races[0].split(" ") if time]
    distance = [int(race) for race in races[1].split(" ") if race]

    def possible_records(time, distance):
        records = []
        for i in range(time):
            if not i:
                continue
            dist = (time - i) * i
            if dist > distance:
                records.append(dist)
        return len(records)

    records = []
    for time, dist in zip(times, distance):
        records.append(possible_records(time, dist))

    return math.prod(records)


def part_two(filename):
    races = load_races(filename)
    time = races[0].replace(" ", "")
    distance = races[1].replace(" ", "")

    def possible_records(time, distance):
        records = []
        for i in range(time):
            if not i:
                continue
            dist = (time - i) * i
            if dist > distance:
                records.append(dist)
        return len(records)

    return possible_records(int(time), int(distance))


def load_races(filename):
    with open(file=filename, mode="r") as f:
        lines = f.read().splitlines()
    return lines


if __name__ == "__main__":
    input_path = "./day_06/input.txt"
    print("------Part One-----")
    print(part_one(input_path))

    print("------Part Two-----")
    print(part_two(input_path))
