from sys import stdin

numbers = [int(number) for number in stdin.read().split()]

print(sum(numbers))
