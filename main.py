from cards import computer_card, player_card, determine_winner
from conditions import checkScores
from scores import scores


def main_game():
    print("Welcome to Critters!")
    while True:
        computer_card_value = computer_card()
        player_card_value = player_card()
        result = determine_winner(card1=computer_card_value, card2=player_card_value)
        print(result)
        print(f"Player Score: {scores.playerScore} | Computer Score: {scores.computerScore}")

        if not checkScores():
            break


if __name__ == "__main__":
    main_game()
