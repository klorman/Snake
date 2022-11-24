import curses
from snake import Snake
from fruit import Fruit


class Field:
	def __init__(self, screen):
		self.screen = screen
		self.size = (curses.LINES, curses.COLS)
		self.snake = Snake()
		self.fruit = Fruit()

	def redraw(self):
		if self.snake.tail_end != self.snake.tails[-1]:
			self.screen.addstr(self.snake.tail_end.position[0], self.snake.tail_end.position[1], ' ')

		objects = self.snake.tails + [self.snake.head, self.fruit]

		for obj in objects:
			self.screen.addstr(obj.position[0], obj.position[1], obj.symbol)

		self.screen.refresh()
