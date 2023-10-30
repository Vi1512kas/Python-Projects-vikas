# TODO: Create a letter using starting_letter.txt
PlaceHolder = "[name]"
with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in names:
        stripped_name = name.strip()
        data = letter_content.replace(PlaceHolder, stripped_name)
        with open(f"Output/ReadyToSend/send_to_{stripped_name}.txt", "w") as file:
            file.write(data)


