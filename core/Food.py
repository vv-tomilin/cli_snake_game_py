import random

class Food:
    def __init__(self, game_place_height, game_place_width):
        self.position = (random.randint(1, game_place_height - 2), random.randint(1, game_place_width - 2))
        self.height = game_place_height
        self.width = game_place_width

    def get_position(self):
        return self.position

    def generate(self):
        food = (random.randint(1, self.height - 2), random.randint(1, self.width - 2))
        self.position = food

    def render(self, stdscr, snake):
        # Еда не должна появляться на змейке
        if self.position not in snake.get_position_head():
            stdscr.addch(self.position[0], self.position[1], "+")