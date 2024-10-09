kids = int(input())
candies = int(input())

candies_per_kid = candies // kids
remaining_candies = candies % kids

print(candies_per_kid, remaining_candies, sep='\n')
