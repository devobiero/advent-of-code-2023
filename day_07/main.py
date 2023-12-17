def part_one(filename):
    hands = [
        "Five of a kind",
        "Four of a kind",
        "Full house",
        "Three of a kind",
        "Two pair",
        "One pair",
        "High card",
    ]
    cards = [card.split(" ") for card in load_hands(filename)]

    def hand_comparator(hand):
        return hands.index(hand[1])

    def card_comparator(card):
        cards_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        return [cards_order.index(char) for char in card[0]]

    def get_hand_type(hand):
        lookup = dict()
        for c in hand:
            lookup[c] = lookup.get(c, 0) + 1

        if 5 in lookup.values():
            return hands[0]
        elif 4 in lookup.values():
            return hands[1]
        elif 3 in lookup.values() and 2 in lookup.values():
            return hands[2]
        elif 3 in lookup.values():
            return hands[3]
        elif list(lookup.values()).count(2) == 2:
            return hands[4]
        elif 2 in lookup.values():
            return hands[5]
        else:
            return hands[6]

    results = []
    for card in cards:
        hand = card[0]
        bid = card[1]
        results.append((hand, get_hand_type(hand), int(bid)))

    results.sort(key=lambda x: (hand_comparator(x), card_comparator(x)))

    winnings = 0
    for i, result in enumerate(results):
        rank = len(results) - i
        winnings += rank * result[2]

    return winnings


def part_two(filename):
    pass


def load_hands(filename):
    with open(file=filename, mode="r") as f:
        lines = f.read().splitlines()
    return lines


if __name__ == "__main__":
    input_path = "./day_07/input.txt"
    print("------Part One-----")
    print(part_one(input_path))

    print("------Part Two-----")
    print(part_two(input_path))
