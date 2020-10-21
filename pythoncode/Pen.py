class   Pen:
	def __init__(self):
		self.__color = 'red'
		self.__cost=340.00

	def  __m1(self):
		print("This is private method")

pobj = Pen()
##print(pobj.__color)
##pobj.m1()
pobj.__m1()
