class   Mobile:
	def  __init__(self):
		self.brandName="abc"   ##instance variable
		self.storageSize="4gb"
		self.cost=200.00

	def    calling(self):
		a ="Hello"
		print(self.brandName+"/"+self.storageSize+"/"+str(self.cost)+"/"+a)


print('first object')
obj =  Mobile()
print(obj.brandName+"/"+obj.storageSize+"/"+str(obj.cost))
obj.calling()

print('second object')
obj1 = Mobile()
obj1.brandName = "xyz"
obj1.storageSize = "8gb"
obj1.cost = 300.00
print(obj1.brandName+"/"+obj1.storageSize+"/"+str(obj1.cost))
