class Rectangle:
	def __init__(self, width, height) -> None:
		self.width = width
		self.height = height

	def set_width(self, width):
		self.width = width

	def set_height(self, height):
		self.height = height

	def get_area(self):
		return self.width * self.height

	def get_perimeter(self):
		return (2 * (self.width + self.height))

	def get_diagonal(self):
		return ((self.width ** 2 + self.height ** 2) ** .5)

	def get_picture(self):
		if(self.width > 50 or self.height > 50):
			return "Too big for picture."
		
		lines = []
		width_spacing = self.width - 2
		height_spacing = self.height - 2
		
		lines.append(self.width * "*")

		for i in range(height_spacing):
			lines.append('*'.ljust(width_spacing + 1) + '*')

		lines.append(self.width * "*")
		
		return '\n'.join(lines)
	
	def get_amount_inside(self, shape):
		width_max_items = self.width // shape.width
		height_max_items = self.height // shape.height
		return width_max_items * height_max_items

	def __repr__(self) -> str:
		return f'{__class__.__name__}(width={self.width}, height={self.height})'


class Square(Rectangle):
	def __init__(self, side) -> None:
		super().__init__(side, side)

	def set_side(self, side):
		self.set_height(side)
		self.set_width(side)

	def __repr__(self) -> str:
		return f'{__class__.__name__}(side={self.height})'


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
