class  Shape:
	def  method1(self):
		print('This is a shape class')

class  Circle(Shape):
	def  method2(self):
		print('This is a circle class')

class   Rect(Shape):
	def  method3(self):
		print('This is a Rect class')

obj=Circle()
obj.method1()
obj.method2()

obj1=Rect()
obj1.method1()
obj1.method3()
