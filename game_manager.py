import curses
from ui import UI
from snake import Snake
from fruit import Fruit
from settings import Settings


class GameManager:
	def __init__(self, screen):
		self.ui = UI(screen)
		self.snake = None
		self.fruit = None
		self.is_game_over = False

	def start_new_game(self) -> bool:
		self.ui.screen.clear()
		self.ui.screen.refresh()
		self.is_game_over = False

		self.snake = Snake()
		self.fruit = Fruit()
		self.ui.create_field()

		self.snake.spawn(self.ui.field.size)
		self.fruit.spawn(self.ui.field.size)

		while not self.is_game_over:
			self.update()
			curses.napms(1000 // self.snake.speed)

			if len(self.snake.tails) + 2 >= Settings.field_size[0] * Settings.field_size[1]:
				return True

		return False

	def is_snake_out_of_field(self):
		return self.snake.head.position[0] < 1 or \
				self.snake.head.position[0] > Settings.field_size[0] or \
				self.snake.head.position[1] < 1 or \
				self.snake.head.position[1] > Settings.field_size[1]

	def process_input(self):
		acceleration_key = ord(' ')

		key = self.ui.screen.getch()
		curses.flushinp()

		if key == acceleration_key:
			self.snake.speed = Settings.snake_speed * 100
		else:
			self.snake.speed = Settings.snake_speed

		self.snake.change_direction(key)

	def update_field(self):
		self.ui.field.redraw(self.snake, self.fruit)

	def update(self):
		self.process_input()

		self.snake.move()

		if self.snake.head in self.snake.tails or self.is_snake_out_of_field():
			self.is_game_over = True
			self.snake.head.symbol = '█'
			self.update_field()
			curses.napms(2000)
			return

		elif self.snake.head == self.fruit:
			self.snake.add_tail()
			while self.fruit == self.snake.head or self.fruit in self.snake.tails: #TODO: переделать
				self.fruit.spawn(self.ui.field.size)

		self.update_field()
