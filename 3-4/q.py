from itertools import chain, combinations, product

suit = input().strip()
rank = input().strip()
hand = input()

suits = {'буби': 'бубен', 'пики': 'пик', 'трефы': 'треф', 'черви': 'червей'}
ranks = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']

ranks.remove(rank)

triplets = combinations(product(ranks, suits.values()), 3)
triplets = [triplet for triplet in triplets if suits[suit] in list(chain.from_iterable(triplet))]
triplets.sort()

print_next = False

for triplet in triplets:
    if print_next:
        print(', '.join(f'{rank} {suit}' for rank, suit in triplet))
        break
    if ', '.join(f'{rank} {suit}' for rank, suit in triplet) == hand:
        print_next = True
