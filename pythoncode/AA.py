class  AA:
	g = 30    ###class variable
	def ___init__(self):
		self.h=7000  ###instance variable

class BB(AA):
	def  m1(self):
		print("base class class variable","/",super().g)
		print("base class instance varile","/",self.h)

obj=BB()
obj.m1()
