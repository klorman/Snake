class FieldObject(object):
	def __init__(self, symbol, position):
		self.symbol = symbol
		self.position = position

	def __eq__(self, other):
		if not isinstance(other, FieldObject):
			return NotImplemented

		return self.position == other.position
