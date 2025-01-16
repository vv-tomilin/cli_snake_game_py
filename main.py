import curses

from playsound import playsound

from modules.start_game import start_game
from core.GamePlace import GamePlace

def main(stdscr):
    game_place = GamePlace(50, 25)
    game_place.render(stdscr=stdscr)

    stdscr.addstr(game_place.get_height() // 2 + 2, game_place.get_width() // 2 - 18, f"Для начала игры нажмите <Enter>!")

    playsound('./sounds/start/mario_bros meloboom.mp3', False)

    while True:
        key = stdscr.getch()
        if key == ord(' '):
            break
        if key == ord('\n'):
            start_game(stdscr=stdscr, game_place=game_place)

if __name__ == "__main__":
    curses.wrapper(main)