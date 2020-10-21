class   OuterClass:
	message = "This is outer class var"
	def  __init__(self):
		self.innerinstance=self.InnerClass()

	class   InnerClass:
		def   printMessage(self):
			return OuterClass.message

outerinstance =  OuterClass()
print(outerinstance.innerinstance.printMessage())
