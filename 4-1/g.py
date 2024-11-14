def can_eat(horse_coordinates, other_coordinates):
    x = abs(horse_coordinates[0] - other_coordinates[0])
    y = abs(horse_coordinates[1] - other_coordinates[1])

    return sorted([x, y]) == [1, 2]

