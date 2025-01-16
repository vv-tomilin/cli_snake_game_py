import curses
import time

from playsound import playsound

from core.GameInfo import GameInfo
from core.Snake import Snake
from core.Food import Food

def start_game(stdscr, game_place):
    curses.curs_set(0)
    stdscr.timeout(150)

    game_place_height = game_place.get_height()
    game_place_width = game_place.get_width()

    game_info = GameInfo()

    snake = Snake(3, game_place)

    food = Food(game_place_height=game_place_height, game_place_width=game_place_width)

    while True:
        key = stdscr.getch()
        snake.direction_control(key=key)

        is_move = snake.move(game_place_height=game_place_height, game_place_width=game_place_width)

        if not is_move:
            break

        stdscr.clear()
        game_place.render(stdscr)
        snake.render(stdscr)

        food_position = food.get_position()
        food.render(stdscr, snake)
        is_eat_food = snake.eat_food(food_position)

        if is_eat_food:
            food.generate()
            food.render(stdscr=stdscr, snake=snake)
            game_info.up_score()

        score = game_info.get_score()
        stdscr.addstr(game_place_height // 1 + 1, game_place_width // 2 - 7, f"Счет: {score}")

    playsound('./sounds/game_over/zvuk_obloma_meloboom.mp3', True)
    playsound('./sounds/game_over/game-over-mario-meloboom.mp3', False)

    stdscr.clear()
    game_place.render(stdscr)
    stdscr.addstr(game_place_height // 3 + 2, game_place_width // 2 - 7, f"Игра окончена!")
    result_score = game_info.get_score()
    stdscr.addstr(game_place_height // 3 + 3, game_place_width // 2 - 7, f"Ваш счёт: {result_score}")
    stdscr.addstr(game_place_height // 3 + 6, game_place_width // 2 - 14, f"Новая игра - нажмите <Enter>")
    stdscr.addstr(game_place_height // 3 + 7, game_place_width // 2 - 12, f"Выйти - нажмите <Пробел>")
    time.sleep(3)
    playsound('./sounds/start/battle_city_main_theme_tanchiki meloboom.mp3', False)
    stdscr.refresh()
    stdscr.nodelay(False)