class GamePlace:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def render(self, stdscr):
        for y in range(self.height):
            for x in range(self.width):
                if y == 0 or y == self.height - 1 or x == 0 or x == self.width - 1:
                    stdscr.addch(y, x, ord("#"))

        stdscr.refresh()