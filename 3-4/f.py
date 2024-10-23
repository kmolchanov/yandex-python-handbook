from itertools import product

suit = input()

denominations = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
suits = ['пик', 'треф', 'бубен', 'червей']

suits.remove(suit)

for denomination, suit in product(denominations, suits):
    print(f'{denomination} {suit}')
