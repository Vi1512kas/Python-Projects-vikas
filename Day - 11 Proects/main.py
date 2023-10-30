import random
from art import logo

def compare(user_score, computer_score):
    if user_score == computer_score:
        print("draw")
    elif computer_score == 0 and user_score != 0:
        print("computer_wins")
    elif computer_score != 0 and user_score == 0:
        print("user_wins")
    elif computer_score > 21:
        print("computer_loses")
    elif user_score > 21:
        print("user loses")
    else:
        if user_score > computer_score:
            print("user_wins")
        else:
            print("computer_wins")


def play_game():
    print(logo)

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        elif sum(cards) > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    is_game_on = True
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while is_game_on:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_on = False
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass:")
            if choice == 'y':
                user_cards.append(deal_card())
            else:
                is_game_on = False
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's cards: {computer_cards}, computer score: {user_score}")
    compare(user_score, computer_score)


while input("Type 'y' to play another game") == 'y':
    play_game()
