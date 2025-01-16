class GameInfo:
    def __init__(self):
        self.score = 0

    def get_score(self):
        return self.score

    def up_score(self):
        self.score += 1