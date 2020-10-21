class  A:
    def m1(self):
	       print('A class method')

class B(A):
    def m1(self):
            print("B class method")

class C(B):
	def m1(self):
			print("c class method")

class D(C):
    def m1(self):
        B.m1(self)
        super(D,self).m1()

d = D()
d.m1()
