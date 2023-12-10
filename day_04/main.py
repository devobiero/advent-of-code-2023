def part_one(filename):
    cards = read_cards(filename)
    total = 0

    for card in cards:
        _, played, winners = card
        played = played.split(" ")
        winners = winners.split(" ")

        i = 0
        count = 0
        points = 0

        while i < len(played):
            if played[i] and played[i] in winners:
                count += 1
                points = points * 2 if count > 1 else 1

            i += 1
        total += points

    return total


def part_two(filename):
    cards = read_cards(filename)
    copies = []

    for card in cards:
        card_number, played, winners = card
        played = played.split(" ")
        winners = winners.split(" ")

        i = 0
        count = 0

        while i < len(played):
            if played[i] and played[i] in winners:
                count += 1
            i += 1

        num = int(card_number)
        extra = copies.count(num)
        next_card = num + 1
        tmp = []
        copies.append(num)

        while count > 0:
            tmp.append(next_card)
            next_card += 1
            count -= 1

        copies.extend(tmp)

        while extra > 0:
            copies.extend(tmp)
            extra -= 1

    return len(copies)


def read_cards(filename):
    with open(file=filename, mode="r") as f:
        lines = f.read().split("\n")
        cards = []
        for line in lines:
            data = line.split(" | ")
            card = data[0].split(": ")
            cards.append((card[0].split("Card")[1].strip(), card[1], data[1]))

    return cards


if __name__ == "__main__":
    input_path = "./day_04/input.txt"
    print("------Part One-----")
    print(part_one(input_path))

    print("------Part Two-----")
    print(part_two(input_path))
