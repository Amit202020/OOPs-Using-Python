class  Shape:
	def  area(self):
		print('This is shape class')

class  Circle(Shape):
	def  area1(self):
		print('This s circle class')

obj = Circle()
obj.area()
obj.area1()
