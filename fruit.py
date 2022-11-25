from random import randrange
from field_object import FieldObject


class Fruit(FieldObject):
	def __init__(self):
		self.need_to_redraw = True
		super().__init__('@', (None, None))

	def spawn(self, size):
		self.need_to_redraw = True
		self.position = (randrange(1, size[0] - 2), randrange(1, size[1] - 2))