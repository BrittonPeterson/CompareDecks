def create_deck():
	deck = {}
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
	
num_of_decks = int(input("Enter the number of decks you would like to compare: "))
deck_index = create_deck()

for d in range(num_of_decks):
	print(f"\nCards that appear {d+1} times: ")
	for card in deck_index:
		if deck_index[card] == (d+1):
			print(card[2:])
