class   Product:
    pname ="electronics"     ##class variable
    def  __init__(self,pid,pname,pdesc):
        self.prodId = pid
        self.prodName = pname
        self.prodDesc = pdesc

    def  method1(self):     ##instance method
        print(str(self.prodId)+"/"+self.prodName+"/"+self.prodDesc)

    @classmethod
    def  method2(cls):        ##class method
        print('Name of the product is '+ cls.pname)


    @staticmethod
    def  method3():     ## utility method
        print('This is static method')



obj  = Product(999,'device','50 feet long')
obj.method1()

obj1 = Product(998,'food','non veg')
Product.method2()

obj2 = Product(997,'drink','qqqqq')
Product.method3()
