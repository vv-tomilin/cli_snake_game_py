import curses
import random

from playsound import playsound
souds_list = [
    'bubble-popping meloboom.mp3',
    'catchphrase meloboom.mp3',
    'comic-spring meloboom.mp3',
    'cuack-sound meloboom.mp3',
    'fart-sm meloboom.mp3',
    'krik_letyaschej_ptichki_iz_igry_angry_birds_2 meloboom.mp3',
    'toasty meloboom.mp3',
    'tweet-tweet-sms meloboom.mp3',
    'weird-pium meloboom.mp3'
]

class Snake:
    def __init__(self, length, game_place):
        self.length = length
        self.position = [(game_place.get_height() // 2, game_place.get_width() // 2)]
        self.direction = [0, 1]

    def get_lenght(self):
        return self.length

    def get_position_head(self):
        return self.position

    def move(self, game_place_height, game_place_width):
        head_y, head_x = self.position[0]
        delta_y, delta_x = self.direction
        new_head = (head_y + delta_y, head_x + delta_x)
        self.position.insert(0, new_head)

        if len(self.position) > self.length:
            self.position.pop()

        if (new_head[0] < 0 or new_head[0] >= game_place_height) or \
           (new_head[1] < 0 or new_head[1] >= game_place_width):
                return False
        else:
            return True

    def direction_control(self, key):
        if key == curses.KEY_UP:
            if self.direction != [1, 0]:
                self.direction = [-1, 0]
        elif key == curses.KEY_DOWN:
            if self.direction != [-1, 0]:
                self.direction = [1, 0]
        elif key == curses.KEY_RIGHT:
            if self.direction != [0, -1]:
                self.direction = [0, 1]
        elif key == curses.KEY_LEFT:
            if self.direction != [0, 1]:
                self.direction = [0, -1]

    def eat_food(self, food_position):
        head_y, head_x = self.position[0]
        food_y, food_x = food_position

        if head_y == food_y and head_x == food_x:
            rand_sound_item = random.randint(0, len(souds_list) - 1)
            playsound(f'./sounds/eat/{souds_list[rand_sound_item]}', False)

            self.length += 1
            return True
        else:
            return False

    def render(self, stdscr):
        for y, x in self.position:
            stdscr.addch(y, x, "*")

        stdscr.refresh()