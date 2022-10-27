from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score} High Score: {self.high_score}", True, align="center",
                   font=("Courier", 12, 'normal'))

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.reset_high_score()
        self.score = 0
        self.update_scoreboard()

    @staticmethod
    def get_high_score():
        with open("data.txt") as data:
            high_score = int(data.read())
            return high_score

    def reset_high_score(self):
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))

