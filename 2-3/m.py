number_of_players = int(input())

first_player_name = player_name = input()

for _ in range(number_of_players - 1):
    player_name = input()
    if first_player_name > player_name:
        first_player_name = player_name

print(first_player_name)
