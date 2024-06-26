from scores import scores


def checkScores():
    if scores.playerScore == 4 or scores.computerScore == 4:
        return GameOver()
    return True


def GameOver():
    if scores.playerScore == 4:
        print("Congratulations, you won!")
        scores.increment_player_games_won()
    elif scores.computerScore == 4:
        print("You lost. Better luck next time!")
        scores.increment_computer_games_won()

    print(f"Player: {scores.playerGamesWon} | Computer: {scores.computerGamesWon}")

    while True:
        play_again = input("Do you want to play again? \n"
                           "1. Yes\n"
                           "2. No\n")
        if play_again == '1':
            scores.reset_scores()
            return True
        elif play_again == '2':
            scores.reset_scores()
            scores.reset_games_won()
            return False
        else:
            print("Invalid input. Please enter 1 for 'yes' or 2 for 'no'.")
