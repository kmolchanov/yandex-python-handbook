from itertools import product, chain, permutations

suit, denomination = input(), input()

denominations = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
suits = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}

denominations.remove(denomination)

triplets = permutations(product(denominations, suits.values()), 3)

triplets = [triplet for triplet in triplets if suits[suit] in chain.from_iterable(triplet)]

sorted_combinations = sorted(triplets)
for combination in sorted_combinations[:10]:
    print(', '.join(f'{rank} {suit}' for rank, suit in combination))
