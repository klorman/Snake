import curses
from input import Input


class Menu(object):
    def __init__(self, screen, options, title):
        self.screen = screen
        self.options = options
        self.title = title
        self.selected_line = 0

    def show(self) -> None:
        self.screen.clear()
        y_size, x_size = self.screen.getmaxyx()

        title_lines = self.title.split('\n')

        if len(self.title) > 0:
            y = 5
            x = x_size // 2 - len(title_lines[0]) // 2

            if y >= 0 and not (x < 0 or x > x_size):
                for line in title_lines:
                    self.screen.addstr(y, x, line)
                    y += 1

        for i, option in enumerate(self.options):
            option = str(option)

            x = x_size // 2 - len(option) // 2

            if len(self.title) > 0:
                y += 2

            if y < 0 or y >= y_size:
                continue
            if x < 0 or x > x_size:
                raise Exception('Increase terminal size')

            if i == self.selected_line:
                self.screen.addstr(y, x, option, curses.A_STANDOUT)
            else:
                self.screen.addstr(y, x, option)

        self.screen.refresh()

    def select(self) -> int:
        while True:
            self.show()

            key = self.screen.getch()

            if key in Input.up or key in Input.left:
                if self.selected_line > 0:
                    self.selected_line -= 1
                else:
                    self.selected_line = len(self.options) - 1

            elif key in Input.down or key in Input.right:
                if self.selected_line < len(self.options) - 1:
                    self.selected_line += 1
                else:
                    self.selected_line = 0

            elif key in [ord('\n'), ord('\r'), curses.KEY_ENTER]:
                return self.selected_line
            else:
                pass
