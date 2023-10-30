import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
data.to_dict()
data_1 = {row.letter: row.code for (index, row) in data.iterrows()}
name = input("Enter Name :").upper()
answer = [data_1[letter] for letter in name]
print(answer)
