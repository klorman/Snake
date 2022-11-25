import curses
from snake import Snake
from fruit import Fruit
from field_object import FieldObject


class Field:
	def __init__(self, screen):
		self.screen = screen
		self.screen.border()
		self.size = screen.getmaxyx()

	def draw_field_object(self, obj: FieldObject):
		self.screen.addstr(obj.position[0], obj.position[1], obj.symbol)

	def redraw(self, snake, fruit):
		self.redraw_snake(snake)
		self.draw_fruit(fruit)

		self.screen.refresh()

	def draw_fruit(self, fruit: Fruit):
		if fruit.need_to_redraw:
			fruit.need_to_redraw = False
			self.draw_field_object(fruit)

	def redraw_snake(self, snake: Snake):
		if snake.is_ate_fruit():
			self.draw_field_object(snake.erasing_tail)

		self.draw_field_object(snake.head)
		self.draw_field_object(snake.tails[0])
