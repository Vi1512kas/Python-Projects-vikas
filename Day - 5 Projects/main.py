# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter = "".join(random.sample(letters, nr_letters))
number = "".join(random.sample(numbers, nr_numbers))
symbol = "".join(random.sample(symbols, nr_symbols))
print("Here is Your Password : "+letter+number+symbol)


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
letter = random.sample(letters, nr_letters)
number = random.sample(numbers, nr_numbers)
symbol = random.sample(symbols, nr_symbols)
output = []
for i in letter:
    output.append(i)
for i in number:
    output.append(i)
for i in symbol:
    output.append(i)
random.shuffle(output)
out = "".join(output)
print("Here is Your Password : "+out)
