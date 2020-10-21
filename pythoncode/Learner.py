class   Learner:
    def  setName(self,name):
	       self.name=name

    def  getName(self):
	       return self.name

    def  setPhone(self,phone):
	       self.phone=phone

    def getPhone(self):
	       return self.phone



nm = input('enter your name')
ph = input('enter your phone')
obj = Learner()
obj.setName(nm)
obj.setPhone(ph)

print('Your name is '+ obj.getName())
print("your mob number is "+ obj.getPhone())
