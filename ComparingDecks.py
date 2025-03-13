def create_deck():
	deck = {}
	num_of_decks = int(input("Enter the number of decks you would like to compare:"))
	for i in range(num_of_decks):
		print(f"Paste the decklist for deck {i+1}, then type done")
		user_input = []
		while True:
			line = input().strip()
			if line.lower() == 'done':
				break
			user_input.append(line)
			
		for card in user_input:
			if card == "SIDEBOARD:":
				break
			if card in deck:
				deck[card] += 1
			else:
				deck[card] = 1
	return deck
	
deck_index = create_deck()

print("Cards that appear thrice:")
for card in deck_index:
	if deck_index[card] == 3:
		print(card)

print("\nCards with that appear twice:")
for card in deck_index:
	if deck_index[card] == 2:
		print(card)

print("\nCards with that appear once:")
for card in deck_index:
	if deck_index[card] == 1:
		print(card)
