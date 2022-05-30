placeHolder = "[name]"
with open("./Input/Names/invited_names.txt") as name:
    names = name.readlines()
with open("./Input/Letters/starting_letter.txt") as card:
    cards = card.read()
    for name1 in names:
        new_cards = name1.strip()
        new_card = cards.replace(placeHolder, new_cards)
        with open(f"./Output/ReadyToSend/letter_for_{new_cards}.txt", mode="w") as completed_card:
            completed_card.write(new_card)


