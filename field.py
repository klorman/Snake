import curses
from snake import Snake
from fruit import Fruit
from field_object import FieldObject


class Field:
	def __init__(self, screen):
		self.screen = screen
		self.size = (curses.LINES, curses.COLS)
		self.snake = Snake()
		self.fruit = Fruit()

	def draw_field_object(self, obj: FieldObject):
		self.screen.addstr(obj.position[0], obj.position[1], obj.symbol)

	def redraw(self):
		self.redraw_snake()
		self.redraw_fruit()

		self.screen.refresh()

	def redraw_fruit(self):
		if self.fruit.need_to_redraw:
			self.fruit.need_to_redraw = False
			self.draw_field_object(self.fruit)

	def redraw_snake(self):
		if self.snake.is_ate_fruit():
			self.draw_field_object(FieldObject(' ', self.snake.tail_end.position))

		self.draw_field_object(self.snake.head)
		self.draw_field_object(self.snake.tails[0])
