from field_object import FieldObject
from input import Input


class SnakeHead(FieldObject):
	def __init__(self, position):
		super().__init__('%', position)
		
		
class SnakeTail(FieldObject):
	def __init__(self, position):
		super().__init__('#', position)


class Snake:
	def __init__(self):
		self.speed = 5
		self.direction = (0, 1)
		self.head = SnakeHead((None, None))
		self.tails = []
		self.tail_end = SnakeTail((None, None))

	def spawn(self, size):
		self.head.position = (size[0] // 2, 2)
		self.tails.append(SnakeTail((self.head.position[0], self.head.position[1] - 1)))
		
	def add_tail(self):
		self.tails.append(self.tail_end)

	def move(self):
		self.tail_end.position = self.tails[-1].position
		self.tails = [SnakeTail(self.head.position)] + self.tails[:-1]
		self.head.position = (self.head.position[0] + self.direction[0], self.head.position[1] + self.direction[1])

	def change_direction(self, input):
		new_direction = None

		if input in Input.left:
			new_direction = (0, -1)
		elif input in Input.right:
			new_direction = (0, 1)
		elif input in Input.up:
			new_direction = (-1, 0)
		elif input in Input.down:
			new_direction = (1, 0)
		else:
			return

		if self.direction[0] != -new_direction[0] and self.direction[1] != -new_direction[1]:
			self.direction = new_direction
		
		
