import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

lenNames = len(names) - 1
bankerRoulette = random.randint(0,lenNames)

print(f"{names[bankerRoulette]} is going to buy the meal today!")