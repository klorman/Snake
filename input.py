import curses


class Input:
    left = [curses.KEY_LEFT, ord('a'), ord('ф')]
    right = [curses.KEY_RIGHT, ord('d'), ord('в')]
    up = [curses.KEY_UP, ord('w'), ord('ц')]
    down = [curses.KEY_DOWN, ord('s'), ord('ы')]