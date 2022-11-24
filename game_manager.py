import time
import curses
from field import Field


class GameManager:
	def __init__(self, screen):
		self.field = Field(screen)
		self.is_game_over = False

	def start_new_game(self):
		curses.update_lines_cols()
		self.is_game_over = False
		self.field = Field(self.field.screen)

		self.field.screen.clear()
		self.field.screen.border()

		self.field.snake.spawn(self.field.size)
		self.field.fruit.spawn(self.field.size)
		
		while not self.is_game_over:
			time.sleep(1 / self.field.snake.speed)
			self.update()

		return False

	def is_snake_out_of_field(self):
		return (self.field.snake.head.position[0] < 1 or self.field.snake.head.position[0] > self.field.size[0] - 2) or \
				(self.field.snake.head.position[1] < 1 or self.field.snake.head.position[1] > self.field.size[1] - 2)

	def update(self):
		key = self.field.screen.getch()
		self.field.snake.change_direction(key)

		self.field.snake.move()

		if self.field.snake.head in self.field.snake.tails or self.is_snake_out_of_field():
			self.is_game_over = True

		elif self.field.snake.head == self.field.fruit:
			self.field.snake.add_tail()
			while self.field.fruit == self.field.snake.head or self.field.fruit in self.field.snake.tails: #TODO: переделать
				self.field.fruit.spawn(self.field.size)

		self.field.redraw()
