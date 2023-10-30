import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)
# print(hangman_art.emoji,end=' ')
print(f"you have {lives * hangman_art.life} life.")

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You had already guessed'{guess}'.")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(
            f"You have chosen a wrong word \"{guess}\", You lose a life.                                  Remaining_Lives =",
            end=' ')
        lives -= 1
        print(lives * hangman_art.life)
        if lives == 0:
            end_of_game = True
            print(hangman_art.lose)

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print(hangman_art.won)

    print(hangman_art.stages[lives])
    print("---------------------------------")
print(f'The solution is {chosen_word}.')
