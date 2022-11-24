import curses
from game_manager import GameManager
from main_menu import MainMenu


def main(screen):
    curses.curs_set(False)
    screen.nodelay(True)
    
    gm = GameManager(screen)
    menu = MainMenu(screen, gm)
    menu.start_routine()


if __name__ == "__main__":
    curses.update_lines_cols()
    curses.wrapper(main)
