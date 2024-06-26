class Score:
    def __init__(self):
        self.computerScore = 0
        self.playerScore = 0
        self.computerGamesWon = 0
        self.playerGamesWon = 0

    def increment_computer_score(self):
        self.computerScore += 1

    def increment_player_score(self):
        self.playerScore += 1

    def reset_scores(self):
        self.computerScore = 0
        self.playerScore = 0

    def increment_computer_games_won(self):
        self.computerGamesWon += 1

    def increment_player_games_won(self):
        self.playerGamesWon += 1

    def reset_games_won(self):
        self.computerGamesWon = 0
        self.playerGamesWon = 0


scores = Score()
