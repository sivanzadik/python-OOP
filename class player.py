class Player:
    def __init__(self, username):
        self.username = username
        self.score = 0
        self.lives = 3

    def add_score(self, points):
        self.score += points

    def lose_life(self):
        self.lives -= 1

    def show_status(self):
        print(f"{self.username} | Score: {self.score} | Lives: {self.lives}")


# Usage
p = Player("Dani")
p.add_score(10)
p.lose_life()
p.show_status()