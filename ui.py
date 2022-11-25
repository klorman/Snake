import curses
from field import Field
from settings import Settings


class UI:
    def __init__(self, screen):
        self.screen = screen
        self.screen_size = screen.getmaxyx()
        self.field = None

    def create_field(self):
        field_screen = self.screen.subwin(Settings.field_size[0] + 2,
                                          Settings.field_size[1] + 2,
                                          (self.screen_size[0] - Settings.field_size[0]) // 2,
                                          (self.screen_size[1] - Settings.field_size[1]) // 2)
        self.field = Field(field_screen)
