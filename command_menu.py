from typing import Callable
from menu import Menu


class CommandMenu(Menu):
    class MenuOption(object):
        def __init__(self, name, cmd):
            self.name = name
            self.cmd = cmd

        def __str__(self) -> str:
            return self.name

    def __init__(self, screen, options, title):
        super().__init__(screen, options, title)

    def cmd(self, num: int) -> Callable[[], str]:
        return self.options[num].cmd

    def start_routine(self):
        while True:
            option = self.options[self.select()].cmd
            if option is None:
                break

            result = option()
            if result is None:
                break
