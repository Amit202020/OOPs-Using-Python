class  AA :
    def  __init__(self,a,b):
        self.x =a
        self.y =b
        print("AA constructor","/",self.x,"/",self.y)

    def  method1(self):
        print("this is base class method")

class  BB(AA):
    def  __init__(self,a,b,c):
		##self.x =a
		##self.y=b
        super().__init__(a,b)
        self.z=c
        print("BB constructor","/",self.x,"/",self.y,"/",self.z)

    def   method2(self):
        super().method1()
        print("this is derived class constructor")



obj1 = BB(40,50,60)
obj1.method2()
