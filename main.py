import curses
from game_manager import GameManager


def main(screen):
    screen.border()
    screen.refresh()
    curses.curs_set(False)
    screen.nodelay(True)
    
    gm = GameManager(screen)
    gm.start_new_game()


if __name__ == "__main__":
    curses.update_lines_cols()
    curses.wrapper(main)
