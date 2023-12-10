def part_one(filename):
    cards = read_cards(filename)
    total = 0

    for card in cards:
        played, winning_number = card
        hands = played.split(" ")
        winners = winning_number.split(" ")
        i = 0
        count = 0
        points = 0

        while i < len(hands):
            if not hands[i]:
                i += 1
                continue

            if hands[i] in winners:
                count += 1
                points = points * 2 if count > 1 else 1

            i += 1
        total += points

    return total


def part_two(filename):
    pass


def read_cards(filename):
    with open(file=filename, mode="r") as f:
        lines = f.read().split("\n")
        cards = []
        for line in lines:
            data = line.split(" | ")
            cards.append((data[0].split(": ")[1], data[1]))

    return cards


if __name__ == "__main__":
    input_path = "./day_04/input.txt"
    print("------Part One-----")
    print(part_one(input_path))

    print("------Part Two-----")
    print(part_two(input_path))
