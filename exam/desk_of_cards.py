cards = input().split(", ")

number_of_lines = int(input())

for line in range(1, number_of_lines + 1):
    command = input()

    if "Add" in command:
        task, card = command.split(", ")
        if card in cards:
            print("Card is already in the deck")
        else:
            cards.append(card)
            print("Card successfully added")

    elif "Remove" in command and "At" not in command:
        task, card = command.split(", ")
        if card in cards:
            cards.remove(card)
            print("Card successfully removed")
        else:
            print("Card not found")

    elif "Remove At" in command:
        task, index = command.split(", ")
        index = int(index)
        if 0 < index < len(cards):
            cards.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")

    elif "Insert" in command:
        task, index, card = command.split(", ")
        index = int(index)
        if 0 < index < len(cards):
            if card in cards:
                print("Card is already added")
            else:
                cards.insert(index, card)
                print("Card successfully added")
            pass
        else:
            print("Index out of range")

print(", ".join(cards))

