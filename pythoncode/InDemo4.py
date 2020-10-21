class   AA:
	def m1(self):
		print("This is AA class m1() ")

class  BB:
	def m1(self):
		print("This is the BB class m1 method")


class   CC(AA,BB):pass


obj=CC()
obj.m1()
