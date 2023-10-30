# Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()
count_1 = 0
count_2 = 0
count_1 += (name1+name2).count("t")
count_1 += (name1+name2).count("r")
count_1 += (name1+name2).count("u")
count_1 += (name1+name2).count("e")
count_2 += (name1+name2).count("l")
count_2 += (name1+name2).count("o")
count_2 += (name1+name2).count("v")
count_2 += (name1+name2).count("e")
total_score = str(count_1)+str(count_2)
total_score = int(total_score)
if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score <= 50 and total_score >= 40:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
    