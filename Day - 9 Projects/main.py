import os

# HINT: You can call clear() to clear the output in the console.
import art

print(art.logo)
flag = True
while flag:
    name = input("What is your Name ?:")
    bid = int(input("What is Your Bid?$"))

    choice = input("Are there any other bidder? Type yes or no \n")
    dic = {}
    dic[name] = bid
    if choice == "no":
        flag = False
        max = 0
        nam = ""
        for i in dic:
            if dic[i] > max:
                nam = i
                max = dic[i]
        print(f"The winner is {nam} with bid ${max}.")
    else:
        os.system('cls||clear')
