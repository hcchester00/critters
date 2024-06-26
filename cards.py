import random
from scores import scores

cards = {
    "Fox": ["Cat"],
    "Cat": ["Mouse"],
    "Mouse": ["Elephant"],
    "Elephant": ["Fox", "Cat"]
}


def determine_winner(card1, card2):
    if card1 in cards[card2]:
        scores.increment_player_score()
        return f"Player's {card2} beats the Computer's {card1}!"
    elif card2 in cards[card1]:
        scores.increment_computer_score()
        return f"Computer's {card1} beats the Player's {card2}!"
    else:
        return f"Computer played {card1}! Player played {card2}! Neither card beats the other!"


def computer_card():
    playable_cards = ["Fox", "Elephant", "Mouse", "Cat"]
    c_card = random.choice(playable_cards)
    return c_card


def player_card():
    while True:
        choice = input("Choose your card: \n"
                       "1. Fox \n"
                       "2. Cat \n"
                       "3. Mouse \n"
                       "4. Elephant \n"
                       "q. Quit Game\n")
        if choice == '1':
            return "Fox"
        elif choice == '2':
            return "Cat"
        elif choice == '3':
            return "Mouse"
        elif choice == '4':
            return "Elephant"
        elif choice.lower() == 'q':
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid choice. Please select again.")