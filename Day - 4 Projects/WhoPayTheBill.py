# Take a list of names and generate who will pay the bill.
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
choice = random.randint(0, len(names)-1)
print(f"{names[choice]} is going to buy the meal today!")
